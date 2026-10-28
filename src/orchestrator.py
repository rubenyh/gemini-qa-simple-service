from model_provider import generate

SYSTEM_CONTEXT = "You are a helpul assitan. Respond concisey"

async def answer_question(user_question: str) -> str:
    prompt = f"{SYSTEM_CONTEXT}\n\nUser question: {user_question}"
    return await generate(prompt)
