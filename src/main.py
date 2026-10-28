from fastapi import FastAPI
from data_models import QuestionRequest, AnswerResponse
import orchestrator

app = FastAPI(title="FAQ AI", description="An AI-powered FAQ application using FastAPI and Google GenAI.")

@app.get("/")
async def root():
    return {"message": "Welcome to the FAQ AI application."}

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.post("/ask", response_model=AnswerResponse)
async def ask(request: QuestionRequest):
    answer = await orchestrator.answer_question(request.question)
    return AnswerResponse(answer=answer)
