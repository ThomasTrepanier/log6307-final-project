import os
import tempfile

from fastapi import FastAPI, Depends
from fastapi.responses import FileResponse


app = FastAPI()


def create_temp_file():
    fd, path = tempfile.mkstemp(suffix='.txt')
    with os.fdopen(fd, 'w') as f:
        f.write('TEST\n')
    try:
        yield path
    finally:
        os.unlink(path)


@app.post("/send")
async def send(file_path=Depends(create_temp_file)):
    return FileResponse(file_path)
