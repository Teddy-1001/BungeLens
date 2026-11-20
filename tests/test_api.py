import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import pymupdf
from fastapi.testclient import TestClient

from app.gemini_service import GeminiConfigurationError

TEMPORARY_DIRECTORY = tempfile.TemporaryDirectory()
os.environ["DATABASE_URL"] = ""
os.environ["BUNGELENS_DATABASE_PATH"] = str(
    Path(TEMPORARY_DIRECTORY.name) / "api.sqlite3"
)

from app.main import app


class ApiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.client_context = TestClient(app)
        cls.client = cls.client_context.__enter__()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client_context.__exit__(None, None, None)
        TEMPORARY_DIRECTORY.cleanup()

    def test_backend_starts_without_gemini_credentials_and_seeds_lessons(self) -> None:
        health = self.client.get("/api/health")
        self.assertEqual(health.status_code, 200)
        self.assertEqual(health.json()["database"], "sqlite")
        response = self.client.get("/api/lessons")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["total"], 6)
        self.assertEqual(
            self.client.get("/api/lessons/constitution-rights").json()["title"],
            "How the Constitution protects your rights",
        )

    def test_document_upload_persists_extracted_text_for_chat(self) -> None:
        document = pymupdf.open()
        page = document.new_page()
        page.insert_text((72, 72), "A person has a right to health care.")
        contents = document.tobytes()
        document.close()

        response = self.client.post(
            "/api/documents/upload",
            files={"file": ("constitution.pdf", contents, "application/pdf")},
        )

        self.assertEqual(response.status_code, 200, response.text)
        document_id = response.json()["item"]["id"]
        listed = self.client.get("/api/documents").json()["items"]
        self.assertTrue(any(item["id"] == document_id for item in listed))

        with patch(
            "app.main.ask_gemini",
            side_effect=GeminiConfigurationError("not configured"),
        ):
            question = self.client.post(
                "/api/chat",
                json={"question": "What right is mentioned?", "document_id": document_id},
            )
        self.assertEqual(question.status_code, 503)

    def test_invalid_upload_is_rejected(self) -> None:
        response = self.client.post(
            "/api/documents/upload",
            files={"file": ("not-a-pdf.pdf", b"not a PDF", "application/pdf")},
        )
        self.assertEqual(response.status_code, 400)

    def test_unmatched_chat_does_not_claim_to_be_grounded(self) -> None:
        response = self.client.post(
            "/api/chat",
            json={"question": "Question with no indexed source terms"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.json()["grounded"])
        self.assertEqual(response.json()["sources"], [])


if __name__ == "__main__":
    unittest.main()
