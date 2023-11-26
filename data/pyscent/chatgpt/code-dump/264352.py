from flask import Flask, request
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

    # Salvam imaginea prelucrata intr-un fisier
    image_prelucrata.save("imagine_prelucrata.jpg")

    return "Imagine prelucrata si salvata cu succes!"
