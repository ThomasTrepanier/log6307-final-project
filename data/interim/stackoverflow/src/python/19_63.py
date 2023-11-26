from fastapi import FastAPI


app = FastAPI(debug=False)


@app.get("/")
async def root():
    return {"message": "hello"}
