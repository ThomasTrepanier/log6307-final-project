from flask import Flask, render_template, jsonify, request
import os
import cv2
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# Load the pre-trained model and set up other necessary variables
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
model = tf.keras.models.load_model('digit_recognizer_model.h5')

def process_image(image):
    img_resized = cv2.resize(image, (28, 28))
    img_inverted = np.invert(img_resized)
    img_expanded = np.expand_dims(img_inverted, axis=0)
    img_expanded = np.expand_dims(img_expanded, axis=-1)
    return img_expanded

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    image_file = request.files['image']
    image_array = np.frombuffer(image_file.read(), np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_GRAYSCALE)

    img_expanded = process_image(image)
    prediction = model.predict(img_expanded)

    return jsonify({'prediction': int(np.argmax(prediction))})

if __name__ == '__main__':
    app.run(debug=True)
