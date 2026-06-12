import os
import sys

from google import genai
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
#genai.configure(api_key=GEMINI_API_KEY)

if not GEMINI_API_KEY:
    print(
        "Error: GEMINI_API_KEY is not set. "
        "Add it to your .env file or environment variables.",
        file=sys.stderr,
    )
    sys.exit(1)

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/test-gemini")
def test_gemini():
    client = genai.Client(api_key=GEMINI_API_KEY)
    model = "gemini-2.5-flash"
    outline_prompt = "Draft a short outline of a blog post about using a RAG system."
    response = client.models.generate_content(model=model, contents=outline_prompt)
    outline_result = response.text
    blog_prompt = "Expand from the outline to write a blog post focusing on the benefits of using a RAG system based on the following outline: " + outline_result
    blog_response = client.models.generate_content(model=model, contents=blog_prompt)
    blog_result = blog_response.text
    return {"response": blog_result}