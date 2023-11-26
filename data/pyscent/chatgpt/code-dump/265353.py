from flask import Flask, request, send_file
from io import BytesIO
from PIL import Image

app = Flask(__name__)

@app.route("/prelucreaza_imagine", methods=["POST"])
def prelucreaza_imagine():
    # Preluam continutul imaginii din formularul postat
    image_file = request.files.get("image")
    image_content = image_file.read()

    # Cream un obiect PIL.Image din continutul imaginii
    image_pil = Image.open(io.BytesIO(image_content))

    # Aplicam o prelucrare asupra imaginii
    image_prelucrata = image_pil.rotate(45)

    # Salvam imaginea prelucrata intr-un obiect BytesIO
    image_buffer = BytesIO()
    image_prelucrata.save(image_buffer, format="JPEG")
    image_bytes = image_buffer.getvalue()

    # Cream un obiect FileStorage din continutul imaginii prelucrate
    image_file_prelucrata = FileStorage(stream=image_bytes, filename=image_file.filename)

    # Returnam raspunsul HTTP cu imaginea prelucrata
    return send_file(image_file_prelucrata, mimetype=image_file_prelucrata.content_type)
