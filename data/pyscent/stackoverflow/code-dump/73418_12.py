from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn
import os

app = FastAPI()

@app.get("/download-file")
def download_file(file_name: str):
    folder_path = r"C:\Users\HP\Desktop\excel files"
    file_location = f'{folder_path}{os.sep}{file_name}.xlsx'#os.sep is used to seperate with a \
    return FileResponse(file_location, media_type='application/octet-stream', filename=file_name)


uvicorn.run(app, port=9105)
