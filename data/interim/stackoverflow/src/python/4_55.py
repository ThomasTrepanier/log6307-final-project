def upload_file(remote_path,local_path):
    try:
        blobService = BlockBlobService(account_name=SETTINGS.AZURE_ACCOUNT_NAME, account_key=SETTINGS.AZURE_ACCOUNT_KEY)
        blobService.create_blob_from_path('data',remote_path,local_path)
    except Exception as e:
        logger.error(f'Unable to save azure blob data. {str(e)}')
        raise Exception(f'Unable to save azure blob data. {str(e)}')
