import os
import sys

from google import genai
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = "gemini-2.5-flash"

if not GEMINI_API_KEY:
    print(
        "Error: GEMINI_API_KEY is not set. "
        "Add it to your .env file or environment variables.",
        file=sys.stderr,
    )
    sys.exit(1)

client = genai.Client(api_key=GEMINI_API_KEY)
app = FastAPI()

class QueryRequest(BaseModel):
    question: str

#simple input validation
def validate_user_input(text: str):
    if text is None or text.strip() == "":
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    if len(text) < 5:
        raise HTTPException(status_code=400, detail="Question is too short")

    if len(text) > 500:
        raise HTTPException(status_code=400, detail="Question is too long")

#simple output validation
def validate_model_output(text: str):
    if text is None or text.strip() == "":
        raise HTTPException(status_code=500, detail="AI returned an empty response")

    if len(text) < 10:
        raise HTTPException(status_code=500, detail="AI response is too short")

#second model call to review the first response
def review_model_output(original_answer: str):
    review_prompt = f"""
You are reviewing an AI-generated response.

Your job:
- If the response is unclear, incomplete, or poorly written, improve it.
- If the response is already good, return it unchanged.

AI response to review:
{original_answer}
"""

    review_response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=review_prompt,
    )

    return review_response.text

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/test-gemini")
def test_gemini():
    outline_prompt = "Draft a short outline of a blog post about using a RAG system."
    response = client.models.generate_content(model=GEMINI_MODEL, contents=outline_prompt)
    outline_result = response.text
    blog_prompt = "Expand from the outline to write a blog post focusing on the benefits of using a RAG system based on the following outline: " + outline_result
    blog_response = client.models.generate_content(model=GEMINI_MODEL, contents=blog_prompt)
    blog_result = blog_response.text
    return {"response": blog_result}

@app.post("/query")
def query_ai(request: QueryRequest):
    validate_user_input(request.question)

    primary_response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=request.question,
    )

    raw_answer = primary_response.text

    validate_model_output(raw_answer)

    reviewed_answer = review_model_output(raw_answer)

    return {
        "question": request.question,
        "answer": reviewed_answer
    }