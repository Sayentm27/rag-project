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

## Multi-Step Execution (WEEK 6)

- with implementing multi-step execution for AI, Gemini is given two prompts to give an acurate and detailed response tailored precisely to what the user needs
    - the first is an outline prompt for background details and important information that the AI should keep in mind for the next response or prompts so it can learn
    - the second prompt asks the AI to expand on the previous response the AI gave
- this seperation, or multi-step execution is important because it breaks down the process to give the user more control over what information is being given, overall allowing a more precise response to what the user wanted to begin with
- essentially, this allows complete control over the process so the AI can create a structure with higher quality that the user likes best

- my multi-step execution specifically requests an outline for a blog and then expand on the information from the outine, but focusing on the benefits of the information requested

##Validating User Input and AI Output

- input validation is important because users can send empty, broken, or malicious input, which can harm the system
- output validation is important because the AI models can hallucinate or return bad, incomplete, or confusing answers
- validation prevents these problems by enforcing guidlines
- a second AI model is used to review responses as a way to validate the inputs and outputs
- if the second AI needed to improve the response from the first AI it can provide feedback on what to improve