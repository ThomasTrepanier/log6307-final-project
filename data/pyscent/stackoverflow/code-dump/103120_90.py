from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.callbacks import TensorBoard
import time
import os 

#load mnist dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

#create and compile the model
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)), 
  tf.keras.layers.Dense(128, activation='relu'), 
  tf.keras.layers.Dropout(0.2), 
  tf.keras.layers.Dense(10, activation='softmax') 
])
model.summary()

# This will work because it makes sense
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=[tf.keras.metrics.SparseCategoricalAccuracy(),
                       tf.keras.metrics.CategoricalCrossentropy()])

# This will not work because it isn't designed for the multiclass classification problem
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=[tf.keras.metrics.SparseCategoricalAccuracy(),
                       tf.keras.metrics.TruePositives()])

#model checkpoint (only if there is an improvement)

checkpoint_path = "logs/weights-improvement-{epoch:02d}-{accuracy:.2f}.hdf5"

cp_callback = ModelCheckpoint(checkpoint_path,
                              monitor='accuracy',
                              save_best_only=True,
                              verbose=1,
                              mode='max')

#Tensorboard
NAME = "tensorboard_{}".format(int(time.time())) # name of the model with timestamp
tensorboard = TensorBoard(log_dir="logs/{}".format(NAME))

#train the model
model.fit(x_train, y_train, epochs=5)

#evaluate the model
model.evaluate(x_test,  y_test, verbose=2)
