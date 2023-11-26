from fastapi import FastAPI
from fastapi.responses import HTMLResponse

class CustomAPI(FastAPI):
    def __init__(self, title: str = "CustomAPI") -> None:
        super().__init__(title=title)

        @self.get('/')
        async def home():
            """
            Home page
            """
            return HTMLResponse("<h1>CustomAPI</h1><br/><a href='/docs'>Try api now!</a>", status_code=status.HTTP_200_OK)
