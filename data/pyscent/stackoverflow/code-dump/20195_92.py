from keras.models import load_model
from keras.layers import Lambda
import tensorflow as tf

import make_model

def learning(test_samples):
    model = load_model('my_model.h5')
