import pickle

def serialize(cnn):
    return pickle.dumps({
        "weights": cnn.model.get_weights(),
        "cnnclass": cnn.__class__
    })

def deserialize(cnn_bytes):
    loaded = pickle.loads(cnn_bytes)
    weights, cnnclass = loaded['weights'], loaded['cnnclass']
    cnninstance = cnnclass()
    cnninstance.model.set_weights(weights)
    return cnninstance
