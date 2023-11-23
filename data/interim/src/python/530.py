from fastapi import FastAPI, HTTPException, status
from app.routes.email_routes import router as email_router
from app.config.settings import Settings
from fastapi.responses import RedirectResponse

app = FastAPI()

app.include_router(email_router, prefix="/email", tags=["Emails"])

# Load settings from the .env file
settings = Settings()

# Access the OpenAI API key using settings.openai_api_key
openai_api_key = settings.openai_api_key

# Create a route that redirects "/" to the FastAPI docs page
@app.get("/")
def root():
    return RedirectResponse("/docs")
