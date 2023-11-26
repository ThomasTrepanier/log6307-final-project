import os
import logging

from fastapi import FastAPI, BackgroundTasks, File, UploadFile

log = logging.getLogger(__name__)

app = FastAPI()

DESTINATION = "/"
CHUNK_SIZE = 2 ** 20  # 1MB


async def chunked_copy(src, dst):
    await src.seek(0)
    with open(dst, "wb") as buffer:
        while True:
            contents = await src.read(CHUNK_SIZE)
            if not contents:
                log.info(f"Src completely consumed\n")
                break
            log.info(f"Consumed {len(contents)} bytes from Src file\n")
            buffer.write(contents)


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    fullpath = os.path.join(DESTINATION, file.filename)
    await chunked_copy(file, fullpath)
    return {"File saved to disk at": fullpath}
