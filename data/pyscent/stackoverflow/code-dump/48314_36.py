from fastapi import APIRouter, File, status, Depends, HTTPException,  UploadFile

import shutil
from pathlib import Path

from database.user_functions import *
from database.auth_functions import *
from database.form_functions import *

from model import *
from model_form import *

file_routes = APIRouter()


# @file_routes.post("/files/")
# async def create_file(file: bytes = File()):
#     return {"file_size": len(file)}


# @file_routes.post("/uploadfile/")
# async def create_upload_file(file: UploadFile):
#     return {"filename": file.filename}


@file_routes.post("/upload-file/")
async def create_upload_file(uploaded_file: UploadFile = File(...)):    

    file_location = f"./{uploaded_file.filename}"
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(uploaded_file.file, file_object)    
    return {"info": f"file '{uploaded_file.filename}' saved at '{file_location}'"}
