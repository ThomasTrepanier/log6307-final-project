import io
from PIL import Image
import pillow_heif
from werkzeug.datastructures import FileStorage

class Converter:

    def convert_heic_to_jpeg(self, file):
        # Check if file is a .heic or .heif file
        if file.filename.endswith(('.heic', '.heif', '.HEIC', '.HEIF')):
            # Open image using PIL
            # image = Image.open(file)

            heif_file = pillow_heif.read_heif(file)
            image = Image.frombytes(
                heif_file.mode,
                heif_file.size,
                heif_file.data,
                "raw",
            )

            # Convert to JPEG
            jpeg_image = image.convert('RGB')

            # Save JPEG image to memory temp_img
            temp_img = io.BytesIO()
            jpeg_image.save(temp_img, format("jpeg"))

            # Reset file pointer to beginning of temp_img
            temp_img.seek(0)

            # Create a FileStorage object
            file_storage = FileStorage(temp_img, filename=f"{file.filename.split('.')[0]}.jpg")

            # Set the mimetype to "image/jpeg"
            file_storage.headers['Content-Type'] = 'image/jpeg'

            return file_storage
        else:
            raise ValueError("File must be of type .heic or .heif")
