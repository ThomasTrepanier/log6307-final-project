from pydantic import BaseModel

class EmailPrompt(BaseModel):
    email_prompt: str

    class Config:
        schema_extra = {
            "example": [
                {
                    "email_prompt": "Dear [Recipient],\n\nI hope this email finds you well..."
                },
                {
                    "email_prompt": "Hello team,\n\nI wanted to share some exciting news with all of you..."
                },
                {
                    "email_prompt": "Hi [Name],\n\nI'm writing to follow up on our previous conversation regarding..."
                }
            ]
        }
