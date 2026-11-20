import os
from pathlib import Path

from dotenv import load_dotenv


# =========================================================
# ENVIRONMENT CONFIGURATION
# =========================================================

BASE_DIR = Path(__file__).resolve().parents[1]

# Load local environment variables.
# Hosting platforms use their dashboard environment variables.
load_dotenv(BASE_DIR / ".env")

MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")


# =========================================================
# CUSTOM EXCEPTIONS
# =========================================================

class GeminiConfigurationError(RuntimeError):
    pass


class GeminiRequestError(RuntimeError):
    pass


# =========================================================
# GEMINI SERVICE
# =========================================================

def ask_gemini(prompt: str) -> str:
    """Send a prompt to Gemini and return its response."""

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise GeminiConfigurationError(
            "GEMINI_API_KEY is not configured in the backend environment."
        )

    try:
        from google import genai
        from google.genai.errors import APIError

    except ImportError as error:
        raise GeminiConfigurationError(
            "The google-genai package is not installed."
        ) from error

    try:
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
        )

        answer = (response.text or "").strip()

        if not answer:
            raise GeminiRequestError(
                "Gemini returned an empty response."
            )

        return answer

    except APIError as error:
        raise GeminiRequestError(
            "Gemini request failed."
        ) from error

    except GeminiRequestError:
        raise

    except Exception as error:
        raise GeminiRequestError(
            "An unexpected error occurred while contacting Gemini."
        ) from error
