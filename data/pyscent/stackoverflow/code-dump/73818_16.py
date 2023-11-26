from fastapi import FastAPI

app = FastAPI()

class Hello(str):
    @app.get("/hello")
    def hello(self):
        return {"Hello": self}
