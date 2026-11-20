import tempfile
import unittest
from pathlib import Path

from app.database import (
    get_record,
    get_record_text,
    initialize_database,
    list_records,
    seed_record_if_missing,
    upsert_record,
)


class DatabaseTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.database_path = Path(self.temporary_directory.name) / "records.sqlite3"
        initialize_database(self.database_path)

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def test_upsert_and_search_records(self) -> None:
        record = {"id": "article-43", "number": "43", "title": "Health rights"}
        upsert_record(
            "article",
            record,
            text_content="Every person has the right to health care services.",
            database_path=self.database_path,
        )

        self.assertEqual(
            get_record("article", "article-43", self.database_path)["title"],
            "Health rights",
        )
        self.assertIn("health care", get_record_text("article", "article-43", self.database_path))
        self.assertEqual(
            [item["id"] for item in list_records("article", "health", self.database_path)],
            ["article-43"],
        )

    def test_seed_does_not_overwrite_existing_editorial_updates(self) -> None:
        original = {"id": "lesson-1", "title": "Original title"}
        seed_record_if_missing("lesson", original, self.database_path)
        upsert_record(
            "lesson",
            {"id": "lesson-1", "title": "Edited title"},
            database_path=self.database_path,
        )
        seed_record_if_missing("lesson", original, self.database_path)

        self.assertEqual(
            get_record("lesson", "lesson-1", self.database_path)["title"],
            "Edited title",
        )

    def test_missing_record_text_is_distinct_from_missing_record(self) -> None:
        upsert_record(
            "bill",
            {"id": "bill-1", "title": "Bill"},
            database_path=self.database_path,
        )

        self.assertEqual(get_record_text("bill", "bill-1", self.database_path), "")
        self.assertIsNone(get_record_text("bill", "missing", self.database_path))


if __name__ == "__main__":
    unittest.main()
