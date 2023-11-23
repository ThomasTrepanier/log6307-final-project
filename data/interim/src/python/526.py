from pydantic import BaseModel

class EmailResponse(BaseModel):
    email_content: str
