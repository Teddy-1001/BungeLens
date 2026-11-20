import hashlib
import re
import sys
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Callable
from urllib.error import URLError
from urllib.parse import unquote, urljoin, urlparse
from urllib.request import Request, urlopen

from app.database import initialize_database, upsert_record


MAX_PAGE_BYTES = 5 * 1024 * 1024
MAX_RECORDS_PER_SOURCE = 50
PARLIAMENT_HOST = "www.parliament.go.ke"
PARLIAMENT_SOURCE = "Parliament of Kenya"


@dataclass(frozen=True)
class SourcePage:
    kind: str
    house: str
    url: str


SOURCE_PAGES = (
    SourcePage(
        "bill",
        "National Assembly",
        "https://www.parliament.go.ke/the-national-assembly/house-business/bills",
    ),
    SourcePage(
        "bill",
        "Senate",
        "https://www.parliament.go.ke/the-senate/house-business/bills",
    ),
    SourcePage(
        "proceeding",
        "National Assembly",
        "https://www.parliament.go.ke/the-national-assembly/house-business/hansard",
    ),
    SourcePage(
        "proceeding",
        "Senate",
        "https://www.parliament.go.ke/the-senate/house-business/hansard",
    ),
)


class _ListingParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[dict[str, str]] = []
        self.rows: list[dict[str, Any]] = []
        self._row: dict[str, Any] | None = None
        self._anchor: dict[str, Any] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "tr":
            self._row = {"links": [], "text": []}
        elif tag == "a":
            self._anchor = {
                "href": attributes.get("href") or "",
                "title": attributes.get("title") or "",
                "text": [],
            }

    def handle_data(self, data: str) -> None:
        if self._anchor is not None:
            self._anchor["text"].append(data)
        if self._row is not None:
            self._row["text"].append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "a" and self._anchor is not None:
            link = {
                "href": self._anchor["href"],
                "title": self._anchor["title"],
                "text": " ".join(" ".join(self._anchor["text"]).split()),
            }
            self.links.append(link)
            if self._row is not None:
                self._row["links"].append(link)
            self._anchor = None
        elif tag == "tr" and self._row is not None:
            self.rows.append(self._row)
            self._row = None


def fetch_official_page(url: str) -> str:
    request = Request(
        url,
        headers={
            "Accept": "text/html",
            "User-Agent": "BungeLens official-record importer",
        },
    )
    try:
        with urlopen(request, timeout=20) as response:
            final_url = urlparse(response.geturl())
            if (
                final_url.scheme != "https"
                or final_url.hostname != PARLIAMENT_HOST
            ):
                raise ValueError("The official Parliament page redirected off-site.")
            content = response.read(MAX_PAGE_BYTES + 1)
            if len(content) > MAX_PAGE_BYTES:
                raise ValueError("The official Parliament page exceeds the size limit.")
            encoding = response.headers.get_content_charset() or "utf-8"
            return content.decode(encoding, errors="replace")
    except URLError as error:
        raise RuntimeError(f"Unable to fetch official source {url}: {error}") from error


def _official_pdf_url(href: str, page_url: str) -> str | None:
    absolute_url = urljoin(page_url, href)
    parsed = urlparse(absolute_url)
    path = unquote(parsed.path).casefold()
    if (
        parsed.scheme != "https"
        or parsed.hostname != PARLIAMENT_HOST
        or "/sites/default/files/" not in path
        or not path.endswith(".pdf")
    ):
        return None
    return absolute_url


def _video_url(href: str, page_url: str) -> str | None:
    absolute_url = urljoin(page_url, href)
    parsed = urlparse(absolute_url)
    if parsed.scheme != "https" or parsed.hostname not in {
        "youtube.com",
        "www.youtube.com",
        "m.youtube.com",
        "youtu.be",
    }:
        return None
    return absolute_url


def _link_title(link: dict[str, str], pdf_url: str) -> str:
    filename = unquote(urlparse(pdf_url).path.rsplit("/", 1)[-1])
    fallback = filename[:-4] if filename.casefold().endswith(".pdf") else filename
    for candidate in (link["text"], link["title"], fallback):
        title = re.sub(r"\s+", " ", candidate).strip()
        if title.casefold().endswith(".pdf"):
            title = title[:-4].strip()
        if title and title.casefold() not in {"download", "view pdf", "pdf"}:
            return title
    return fallback.strip()


def _record_id(kind: str, source_url: str) -> str:
    digest = hashlib.sha256(source_url.encode("utf-8")).hexdigest()[:20]
    return f"{kind}-{digest}"


def _base_record(
    kind: str,
    house: str,
    source_url: str,
    title: str,
    listing_url: str,
) -> dict[str, str]:
    return {
        "id": _record_id(kind, source_url),
        "title": title,
        "house": house,
        "sourceUrl": source_url,
        "sourceName": PARLIAMENT_SOURCE,
        "sourceListingUrl": listing_url,
    }


def parse_bill_records(html: str, source: SourcePage) -> list[dict[str, str]]:
    parser = _ListingParser()
    parser.feed(html)
    records: list[dict[str, str]] = []
    seen_urls: set[str] = set()

    for link in parser.links:
        source_url = _official_pdf_url(link["href"], source.url)
        if not source_url or source_url in seen_urls:
            continue
        title = _link_title(link, source_url)
        if "bill" not in title.casefold():
            continue
        seen_urls.add(source_url)
        records.append(
            _base_record("bill", source.house, source_url, title, source.url)
        )
        if len(records) >= MAX_RECORDS_PER_SOURCE:
            break
    return records


def parse_proceeding_records(
    html: str,
    source: SourcePage,
) -> list[dict[str, str]]:
    parser = _ListingParser()
    parser.feed(html)
    rows = parser.rows or [{"links": parser.links, "text": []}]
    records_by_url: dict[str, dict[str, str]] = {}

    for row in rows:
        videos = [
            video_url
            for link in row["links"]
            if (video_url := _video_url(link["href"], source.url))
        ]
        video_url = videos[0] if videos else None
        for link in row["links"]:
            source_url = _official_pdf_url(link["href"], source.url)
            if not source_url:
                continue
            existing_record = records_by_url.get(source_url)
            if existing_record:
                if video_url:
                    existing_record["videoUrl"] = video_url
                continue
            if len(records_by_url) >= MAX_RECORDS_PER_SOURCE:
                continue
            record = _base_record(
                "proceeding",
                source.house,
                source_url,
                _link_title(link, source_url),
                source.url,
            )
            record["type"] = (
                "Order Paper"
                if "order paper" in record["title"].casefold()
                else "Debate"
            )
            if video_url:
                record["videoUrl"] = video_url
            records_by_url[source_url] = record
    return list(records_by_url.values())


def _document_record(record: dict[str, str], category: str) -> dict[str, str]:
    return {
        "id": record["id"],
        "title": record["title"],
        "description": f"Official {category.lower()} record from Parliament of Kenya.",
        "category": category,
        "sourceUrl": record["sourceUrl"],
        "sourceName": record["sourceName"],
        "house": record["house"],
    }


def sync_official_data(
    fetch_page: Callable[[str], str] | None = None,
    database_path: Path | str | None = None,
) -> dict[str, int]:
    fetch = fetch_page or fetch_official_page
    initialize_database(database_path)
    records_by_kind: dict[str, dict[str, dict[str, str]]] = {
        "bill": {},
        "proceeding": {},
    }

    for source in SOURCE_PAGES:
        html = fetch(source.url)
        if source.kind == "bill":
            records = parse_bill_records(html, source)
        else:
            records = parse_proceeding_records(html, source)
        for record in records:
            records_by_kind[source.kind][record["id"]] = record

    for kind, records in records_by_kind.items():
        for record in reversed(list(records.values())):
            upsert_record(kind, record, database_path=database_path)
            if kind == "bill":
                upsert_record(
                    "document",
                    _document_record(record, "Bill"),
                    database_path=database_path,
                )

    return {
        "bills": len(records_by_kind["bill"]),
        "proceedings": len(records_by_kind["proceeding"]),
        "documents": len(records_by_kind["bill"]),
    }


def main() -> None:
    try:
        counts = sync_official_data()
    except (RuntimeError, ValueError) as error:
        print(f"Official data sync failed: {error}", file=sys.stderr)
        raise SystemExit(1) from error

    print(
        "Official data sync complete: "
        f"{counts['bills']} bills, {counts['proceedings']} proceedings, "
        f"{counts['documents']} library documents."
    )


if __name__ == "__main__":
    main()
