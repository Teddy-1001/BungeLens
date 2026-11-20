import tempfile
import unittest
from pathlib import Path

from app.database import list_records
from app.sync_official_data import (
    SOURCE_PAGES,
    parse_bill_records,
    parse_proceeding_records,
    sync_official_data,
)


class OfficialDataSyncTests(unittest.TestCase):
    def test_bill_parser_keeps_only_official_bill_pdfs(self) -> None:
        source = SOURCE_PAGES[0]
        html = """
        <a href="/sites/default/files/2026-01/The%20Housing%20Bill%2C%202026.pdf">
          THE HOUSING BILL, 2026
        </a>
        <a href="https://example.com/other-bill.pdf">Other Bill</a>
        <a href="/sites/default/files/2026-01/annual-report.pdf">Annual report</a>
        """

        records = parse_bill_records(html, source)

        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["title"], "THE HOUSING BILL, 2026")
        self.assertEqual(records[0]["house"], "National Assembly")
        self.assertTrue(records[0]["sourceUrl"].startswith("https://www.parliament.go.ke/"))

    def test_proceeding_parser_pairs_video_links_with_their_own_rows(self) -> None:
        source = SOURCE_PAGES[2]
        html = """
        <table>
          <tr>
            <td><a href="/sites/default/files/hansard-one.pdf">Hansard One</a></td>
          </tr>
          <tr>
            <td><a href="/sites/default/files/hansard-one.pdf">Hansard One</a></td>
            <td><a href="https://youtu.be/video-one">Plenary video</a></td>
          </tr>
          <tr>
            <td><a href="/sites/default/files/hansard-two.pdf">Hansard Two</a></td>
            <td><a href="https://example.com/video">Other video</a></td>
          </tr>
        </table>
        """

        records = parse_proceeding_records(html, source)

        self.assertEqual(len(records), 2)
        self.assertEqual(records[0]["videoUrl"], "https://youtu.be/video-one")
        self.assertNotIn("videoUrl", records[1])
        self.assertEqual(records[0]["type"], "Debate")

    def test_sync_persists_bills_proceedings_and_library_records(self) -> None:
        pages = {
            SOURCE_PAGES[0].url: (
                '<a href="/sites/default/files/national-bill.pdf">'
                "National Bill</a>"
            ),
            SOURCE_PAGES[1].url: (
                '<a href="/sites/default/files/senate-bill.pdf">'
                "Senate Bill</a>"
            ),
            SOURCE_PAGES[2].url: (
                '<tr><td><a href="/sites/default/files/national-hansard.pdf">'
                "National Hansard</a></td></tr>"
            ),
            SOURCE_PAGES[3].url: (
                '<tr><td><a href="/sites/default/files/senate-hansard.pdf">'
                "Senate Hansard</a></td></tr>"
            ),
        }
        with tempfile.TemporaryDirectory() as temporary_directory:
            database_path = Path(temporary_directory) / "records.sqlite3"
            counts = sync_official_data(
                fetch_page=pages.__getitem__,
                database_path=database_path,
            )
            repeated_counts = sync_official_data(
                fetch_page=pages.__getitem__,
                database_path=database_path,
            )

            self.assertEqual(counts, {"bills": 2, "proceedings": 2, "documents": 2})
            self.assertEqual(repeated_counts, counts)
            self.assertEqual(len(list_records("bill", database_path=database_path)), 2)
            self.assertEqual(
                len(list_records("proceeding", database_path=database_path)),
                2,
            )
            library_records = list_records("document", database_path=database_path)
            self.assertEqual(len(library_records), 2)
            self.assertTrue(all(item["category"] == "Bill" for item in library_records))


if __name__ == "__main__":
    unittest.main()
