from pydantic import BaseModel

class SomeObject(BaseModel):
    some_datetime_in_utc: utc_datetime

    class Config:
        json_encoders = {
            utc_datetime: utc_datetime.to_str
        }
