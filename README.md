# RAG Project

This repository contains my Retrieval-Augmented Generation (RAG) project for the GenAI Secure Coding course.

This project will be built incrementally each week.

## Git Commands Used So Far

- git clone
- git status
- git add
- git commit
- git push

## Understanding Code: set up (WEEK 4)

- env variables are loaded in the rag_app.py through load_dotenv()
- the Gemini API key is read by GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
- Gemini would be configured in the rag_app.py file
- FastAPI is created by app = FastAPI()
- only completed set up, not initiation with the API
- the 'rag_app.py' is important for running the app

## Testing Gemini (WEEK 5)

- the /test-gemini returns a Gemini response by defining the model key, then using it to generate a response using the model variable and contents variable
- contents is the question or prompt that the AI is sent to answer
- the Gemini call lives in the test_gemini()
- the function takes the hardcoded prompt and displays the text response as a JSON
- learned that using the AI can sometimes give outdated information, so it's important to double chack and go over code, and make sure that information is up to date

