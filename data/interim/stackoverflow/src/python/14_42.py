import uvicorn

app = FastAPI()

@app.get("/")
def index():
    return {"index": "root"}

if __name__ == '__main__':

    uvicorn.run(f"{Path(__file__).stem}:app", host="127.0.0.1", port=8888, reload=True)
