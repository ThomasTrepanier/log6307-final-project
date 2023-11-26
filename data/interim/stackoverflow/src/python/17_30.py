from fastapi.responses import FileResponse

@app.get("/")
async def main():
    return FileResponse("your_image.jpeg")
