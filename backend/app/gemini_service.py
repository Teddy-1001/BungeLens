
import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai

# Load the API key from backend/.env
env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(env_path)

# Get the API key securely
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError(
        "Gemini API key not found. Check your backend .env file."
    )

# Connect to Gemini
client = genai.Client(api_key=api_key)

MODEL_NAME = "gemini-3.8-flash"


def ask_gemini(prompt: str) -> str:
    """Send a prompt to Gemini and return its response."""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text or "Gemini returned an empty response."
