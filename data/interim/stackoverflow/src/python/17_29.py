from fastapi import FastAPI, Response

app = FastAPI()

@app.post("/vector_image/")
async def image_endpoint():
    # img = ... # Create the image here
    return Response(content=img, media_type="image/png")
