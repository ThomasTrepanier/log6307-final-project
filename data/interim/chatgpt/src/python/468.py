from fastapi import FastAPI
from app.services.openai_service import generate_email

app = FastAPI()

@app.post("/emails/")
async def create_email(email_prompt: dict):
    email_output = generate_email(email_prompt["email_prompt"])
    return email_output
