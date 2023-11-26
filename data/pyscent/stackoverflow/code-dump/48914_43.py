@router.post(path="/test", tags=['File Upload'])
def color_classification_predict(uploadFile: UploadFile):
    try:
        if uploadFile.filename:
            # saved_dir- directory path where we'll save the uploaded file 
            test_filename = os.path.join(saved_dir, uploadFile.filename)
            with open(test_filename, "wb+") as file_object:
                shutil.copyfileobj(uploadFile.file, file_object)
    except Exception as e:
        raise e
    print('[INFO] Uploaded file saved.')
