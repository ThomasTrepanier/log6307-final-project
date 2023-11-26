model=None
def load_model():

    global model
    model = ResNet50(weights="imagenet")
