from fastapi import FastAPI
from fastapi.responses import FileResponse

file_path = "large-video-file.mp4"
app = FastAPI()

@app.get("/")
def main():
    return FileResponse(path=file_path, filename=file_path, media_type='text/mp4')
