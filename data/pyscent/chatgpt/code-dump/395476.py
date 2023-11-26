from fastapi import APIRouter, Depends
from app.services.openai_service import generate_email
from app.models.schemas import EmailPrompt, EmailResponse

router = APIRouter()

@router.post("/emails/", response_model=EmailResponse)
async def create_email(email_prompt: EmailPrompt):
    email_response = generate_email(email_prompt.email_prompt)
    return email_response
