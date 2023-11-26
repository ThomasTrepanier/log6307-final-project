from pydantic import BaseSettings
from decouple import config

class Settings(BaseSettings):
    openai_api_key: str = config("OPENAI_API_KEY")

    class Config:
        env_file = "/path/to/your/.env"
