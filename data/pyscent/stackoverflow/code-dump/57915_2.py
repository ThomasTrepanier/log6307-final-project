import tempfile
from fastapi import FileResponse


class TempFileResponse(FileResponse):
    def __init__(self, prefix, **params) -> None:
        self.temp_file = tempfile.NamedTemporaryFile(prefix=prefix)
        super().__init__(path=self.temp_file.name, **params)

    def __del__(self):
        # This will delete the file
        self.temp_file.close()


@router.get("/produce-data", response_class=FileResponse)
async def produce() -> FileResponse:
    file_name = "some_file_data.txt"
    logger.info(f"Downloading data as {file_name}")
    response_file = TempFileResponse(prefix="some_file_", filename=file_name)
    with open(response_file.temp_file.name, "w") as f:
        f.write("Hello, world!")
    return response_file
