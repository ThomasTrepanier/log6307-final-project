@router.post("/use_upload_file", response_model=dict)
async def use_uploaded_file(
    file_one: UploadFile = File(),
    file_two: UploadFile = File()
    ):


    file_one_path = save_upload_file(audio_one, Path(f"{unique_id()}"))
    file_two_path = save_upload_file(audio_two, Path(f"{unique_id()}"))

    result = YourFunctionThatUsestheSaveFile(audio_one_path, audio_two_path)

    delete_file(audio_one_path)
    delete_file(audio_two_path)

    return result
