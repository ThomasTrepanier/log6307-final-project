import os
import tempfile

from fastapi import FastAPI
from fastapi.responses import FileResponse

from starlette.background import BackgroundTasks

app = FastAPI()


def remove_file(path: str) -> None:
    os.unlink(path)


@app.post("/send")
async def send(background_tasks: BackgroundTasks):
    fd, path = tempfile.mkstemp(suffix='.txt')
    with os.fdopen(fd, 'w') as f:
        f.write('TEST\n')
    background_tasks.add_task(remove_file, path)
    return FileResponse(path)
