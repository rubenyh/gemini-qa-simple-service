from dotenv import load_dotenv
from fastapi import FastAPI
from google import genai
from models import QuestionRequest, AnswerResponse

load_dotenv()

app = FastAPI(title="FAQ AI", description="An AI-powered FAQ application using FastAPI and Google GenAI.")
client = genai.Client()
MODEL_ID = "gemini-3.8-flash"
SYSTEM_CONTEXT = "You are a helpful assistant. Respond concisely and accurately."

@app.get("/")
async def root():
    return {"message": "Welcome to the FAQ AI application."}

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.post("/ask", response_model=AnswerResponse)
async def ask(request: QuestionRequest):
    prompt = f"{SYSTEM_CONTEXT}\n\nUser question: {request.question}"
    response = await client.aio.models.generate_content(
        model=MODEL_ID,
        contents=prompt,
    )
    return AnswerResponse(answer=response.text)
