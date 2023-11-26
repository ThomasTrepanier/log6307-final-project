from pydantic import BaseModel

class EmailPrompt(BaseModel):
    email_prompt: str

    class Config:
        schema_extra = {
            "example": {
                "email_prompt": "Dear [Recipient],\n\nI hope this email finds you well..."
            }
        }
