from io import BytesIO
import dill,base64,tempfile

#Saving Model as base64
model_json = Keras_model.to_json()

def Base64Converter(ObjectFile):
    bytes_container = BytesIO()
    dill.dump(ObjectFile, bytes_container)
    bytes_container.seek(0)
    bytes_file = bytes_container.read()
    base64File = base64.b64encode(bytes_file)
    return base64File

base64KModelJson = Base64Converter(model_json)  
base64KModelJsonWeights = Base64Converter(Keras_model.get_weights())  

