import os
import sys

from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    print(
        "Error: GEMINI_API_KEY is not set. "
        "Add it to your .env file or environment variables.",
        file=sys.stderr,
    )
    sys.exit(1)

app = FastAPI()
