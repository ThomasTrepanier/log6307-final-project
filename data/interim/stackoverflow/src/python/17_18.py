import io
from PIL import Image
from fastapi.responses import StreamingResponse
@app.get('/images/thumbnail/{filename}',
  response_description="Returns a thumbnail image from a larger image",
  response_class="StreamingResponse",
  responses= {200: {"description": "an image", "content": {"image/jpeg": {}}}})
def thumbnail_image (filename: str):
  # read the high-res image file
  image = Image.open(filename)
  # create a thumbnail image
  image.thumbnail((100, 100))
  imgio = io.BytesIO()
  image.save(imgio, 'JPEG')
  imgio.seek(0)
  return StreamingResponse(content=imgio, media_type="image/jpeg")
