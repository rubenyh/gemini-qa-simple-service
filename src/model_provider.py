from dotenv import load_dotenv
from fastapi import HTTPException
from google import genai
from google.genai import errors

load_dotenv()
MODEL_ID = "gemini-3.8-flash"
client = genai.Client()

async def generate(prompt: str) -> str:
    try:
        response = await client.aio.models.generate_content(
            model=MODEL_ID,
            contents=prompt,
        )
    except errors.APIError as error:
        raise HTTPException(
            status_code=502,
            detail="Error communicating with the AI model: " + str(error)
        ) from error
    return response.text # type: ignore
