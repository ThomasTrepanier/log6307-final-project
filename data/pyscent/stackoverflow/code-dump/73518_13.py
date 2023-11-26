from pydantic import BaseModel

class ResponseData(BaseModel):
    status_code: int
    text: str
    reason: str
    
    class Config:
        orm_mode = True
