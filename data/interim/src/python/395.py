from io import BytesIO
from werkzeug.datastructures import FileStorage
from PIL import Image

@app.route("/prelucreaza_imagine", methods=["POST"])
def prelucreaza_imagine():
    # Preluam continutul imaginii din formularul postat
    image_file = request.files.get("image")
    image_content = image_file.read()
    filename = image_file.filename

    # Cream un obiect PIL.Image din continutul imaginii
    image_pil = Image.open(io.BytesIO(image_content))

    # Aplicam o prelucrare asupra imaginii
    image_prelucrata = image_pil.rotate(45)

    # Cream o imagine de predictie din imaginea prelucrata
    model_ai = MyModel()
    prediction = model_ai.predict(image_prelucrata)
    prediction_image = Image.fromarray(prediction)

    # Salvam imaginea de predictie intr-un obiect BytesIO
    image_buffer = BytesIO()
    prediction_image.save(image_buffer, format="JPEG")
    image_buffer.seek(0)
    prediction_image_content = image_buffer.read()

    # Cream un nou obiect FileStorage din continutul imaginii de predictie
    prediction_image_filename = filename.split(".")[0] + "_prediction." + filename.split(".")[1]
    image_file_prediction = FileStorage(stream=BytesIO(prediction_image_content), filename=prediction_image_filename)

    return render_template("home.html", user=current_user, image_file=image_file_prediction)
