from pydantic import BaseModel

class EmailPrompt(BaseModel):
    email_prompt: str
