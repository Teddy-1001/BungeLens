import json
import os
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator

import psycopg
from dotenv import load_dotenv
from psycopg.rows import dict_row
from psycopg.types.json import Jsonb


PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

DATABASE_URL = os.getenv("DATABASE_URL", "").strip()
DEFAULT_DATABASE_PATH = Path(
    os.getenv(
        "BUNGELENS_DATABASE_PATH",
        PROJECT_ROOT / "app" / "data" / "bungelens.sqlite3",
    )
)


def _uses_postgres(database_path: Path | str | None) -> bool:
    return database_path is None and bool(DATABASE_URL)


def get_database_backend() -> str:
    return "postgresql" if DATABASE_URL else "sqlite"


@contextmanager
def connect(
    database_path: Path | str | None = None,
) -> Iterator[Any]:
    if _uses_postgres(database_path):
        connection = psycopg.connect(DATABASE_URL, row_factory=dict_row)
        try:
            yield connection
            connection.commit()
        except Exception:
            connection.rollback()
            raise
        finally:
            connection.close()
        return

    path = Path(database_path) if database_path is not None else DEFAULT_DATABASE_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    try:
        with connection:
            yield connection
    finally:
        connection.close()


def initialize_database(database_path: Path | str | None = None) -> None:
    if _uses_postgres(database_path):
        schema = """
            CREATE TABLE IF NOT EXISTS civic_records (
                kind TEXT NOT NULL,
                id TEXT NOT NULL,
                payload JSONB NOT NULL,
                text_content TEXT NOT NULL DEFAULT '',
                source_url TEXT NOT NULL DEFAULT '',
                source_name TEXT NOT NULL DEFAULT '',
                created_at TIMESTAMPTZ NOT NULL,
                updated_at TIMESTAMPTZ NOT NULL,
                PRIMARY KEY (kind, id)
            )
        """
        index = """
            CREATE INDEX IF NOT EXISTS civic_records_kind_updated
            ON civic_records (kind, updated_at DESC)
        """
    else:
        schema = """
            CREATE TABLE IF NOT EXISTS civic_records (
                kind TEXT NOT NULL,
                id TEXT NOT NULL,
                payload TEXT NOT NULL,
                text_content TEXT NOT NULL DEFAULT '',
                source_url TEXT NOT NULL DEFAULT '',
                source_name TEXT NOT NULL DEFAULT '',
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL,
                PRIMARY KEY (kind, id)
            )
        """
        index = """
            CREATE INDEX IF NOT EXISTS civic_records_kind_updated
            ON civic_records (kind, updated_at DESC)
        """

    with connect(database_path) as connection:
        connection.execute(
            schema
        )
        connection.execute(index)


def _placeholder(database_path: Path | str | None) -> str:
    return "%s" if _uses_postgres(database_path) else "?"


def _encode_payload(
    record: dict[str, Any],
    database_path: Path | str | None,
) -> Any:
    if _uses_postgres(database_path):
        return Jsonb(record)
    return json.dumps(record, ensure_ascii=False)


def _decode_payload(payload: Any) -> dict[str, Any]:
    if isinstance(payload, str):
        decoded = json.loads(payload)
    else:
        decoded = payload
    if not isinstance(decoded, dict):
        raise ValueError("Stored record payload must be a JSON object.")
    return decoded


def _timestamp_string(value: Any) -> str:
    if isinstance(value, datetime):
        return value.isoformat()
    return str(value)


def _database_timestamp(database_path: Path | str | None) -> datetime | str:
    now = datetime.now(timezone.utc)
    return now if _uses_postgres(database_path) else now.isoformat()


def upsert_record(
    kind: str,
    record: dict[str, Any],
    text_content: str = "",
    database_path: Path | str | None = None,
) -> dict[str, Any]:

    record_id = str(record.get("id", "")).strip()

    if not kind.strip() or not record_id:
        raise ValueError(
            "A record kind and non-empty id are required."
        )

    now = _database_timestamp(database_path)

    source_url = str(
        record.get("sourceUrl")
        or record.get("source_url")
        or ""
    )

    source_name = str(
        record.get("sourceName")
        or record.get("source_name")
        or ""
    )

    placeholder = _placeholder(database_path)
    placeholders = ", ".join([placeholder] * 8)
    with connect(database_path) as connection:
        connection.execute(
            f"""
            INSERT INTO civic_records (
                kind,
                id,
                payload,
                text_content,
                source_url,
                source_name,
                created_at,
                updated_at
            )
            VALUES ({placeholders})
            ON CONFLICT (kind, id)
            DO UPDATE SET
                payload = EXCLUDED.payload,
                text_content = EXCLUDED.text_content,
                source_url = EXCLUDED.source_url,
                source_name = EXCLUDED.source_name,
                updated_at = EXCLUDED.updated_at
            """,
            (
                kind,
                record_id,
                _encode_payload(record, database_path),
                text_content,
                source_url,
                source_name,
                now,
                now,
            ),
        )

    return record


def seed_record_if_missing(
    kind: str,
    record: dict[str, Any],
    database_path: Path | str | None = None,
) -> None:

    record_id = str(record.get("id", "")).strip()

    if not kind.strip() or not record_id:
        raise ValueError(
            "A record kind and non-empty id are required."
        )

    now = _database_timestamp(database_path)

    source_url = str(
        record.get("sourceUrl")
        or record.get("source_url")
        or ""
    )

    source_name = str(
        record.get("sourceName")
        or record.get("source_name")
        or ""
    )

    placeholder = _placeholder(database_path)
    placeholders = ", ".join([placeholder] * 7)
    with connect(database_path) as connection:
        connection.execute(
            f"""
            INSERT INTO civic_records (
                kind,
                id,
                payload,
                source_url,
                source_name,
                created_at,
                updated_at
            )
            VALUES ({placeholders})
            ON CONFLICT (kind, id)
            DO NOTHING
            """,
            (
                kind,
                record_id,
                _encode_payload(record, database_path),
                source_url,
                source_name,
                now,
                now,
            ),
        )


def get_record(
    kind: str,
    record_id: str,
    database_path: Path | str | None = None,
) -> dict[str, Any] | None:

    placeholder = _placeholder(database_path)
    with connect(database_path) as connection:
        row = connection.execute(
            f"""
            SELECT
                payload,
                text_content,
                source_url,
                source_name,
                updated_at
            FROM civic_records
            WHERE kind = {placeholder}
              AND id = {placeholder}
            """,
            (kind, record_id),
        ).fetchone()

    if row is None:
        return None

    record = _decode_payload(row["payload"])

    record["sourceUrl"] = (
        record.get("sourceUrl")
        or row["source_url"]
    )

    record["sourceName"] = (
        record.get("sourceName")
        or row["source_name"]
    )

    record["updatedAt"] = _timestamp_string(row["updated_at"])

    if row["text_content"]:
        record["textAvailable"] = True

    return record


def get_record_text(
    kind: str,
    record_id: str,
    database_path: Path | str | None = None,
) -> str | None:

    placeholder = _placeholder(database_path)
    with connect(database_path) as connection:
        row = connection.execute(
            f"""
            SELECT text_content
            FROM civic_records
            WHERE kind = {placeholder}
              AND id = {placeholder}
            """,
            (kind, record_id),
        ).fetchone()

    if row is None:
        return None

    return row["text_content"]


def list_records(
    kind: str,
    query: str = "",
    database_path: Path | str | None = None,
) -> list[dict[str, Any]]:

    placeholder = _placeholder(database_path)
    order_by = (
        "updated_at DESC, id"
        if _uses_postgres(database_path)
        else "updated_at DESC, id COLLATE NOCASE"
    )
    with connect(database_path) as connection:
        rows = connection.execute(
            f"""
            SELECT
                payload,
                source_url,
                source_name,
                updated_at,
                CASE
                    WHEN length(text_content) > 0
                    THEN 1
                    ELSE 0
                END AS text_available
            FROM civic_records
            WHERE kind = {placeholder}
            ORDER BY {order_by}
            """,
            (kind,),
        ).fetchall()

    records = []

    normalized_query = query.casefold().strip()

    for row in rows:
        record = _decode_payload(row["payload"])

        record["sourceUrl"] = (
            record.get("sourceUrl")
            or row["source_url"]
        )

        record["sourceName"] = (
            record.get("sourceName")
            or row["source_name"]
        )

        record["updatedAt"] = _timestamp_string(row["updated_at"])

        if row["text_available"]:
            record["textAvailable"] = True

        if normalized_query:
            searchable = json.dumps(
                record,
                ensure_ascii=False,
            ).casefold()

            if normalized_query not in searchable:
                continue

        records.append(record)

    return records