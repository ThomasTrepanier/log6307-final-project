import asyncio
import uvicorn
from fastapi import FastAPI
app = FastAPI()

@app.get('/')
async def root():
    print('Sleeping for 10')
    await asyncio.sleep(10)
    print('Awake')
    return {'message': 'hello'}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
