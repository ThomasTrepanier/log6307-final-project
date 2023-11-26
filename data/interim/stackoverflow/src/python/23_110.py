app = FastAPI()

@app.get("/hello/{number}/")
def hello_world_number(number: int):
    return {"msg": "Hello World Number", "number": number}
