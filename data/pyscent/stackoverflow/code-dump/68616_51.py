import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

class ThreeLayerMLP(keras.Model):

  def __init__(self, name=None):
    super(ThreeLayerMLP, self).__init__(name=name)
    self.dense_1 = layers.Dense(64, activation='relu', name='dense_1')
    self.dense_2 = layers.Dense(64, activation='relu', name='dense_2')
    self.pred_layer = layers.Dense(10, name='predictions')

  def call(self, inputs):
    x = self.dense_1(inputs)
    x = self.dense_2(x)
    return self.pred_layer(x)

def get_model():
  return ThreeLayerMLP(name='3_layer_mlp')

model = get_model()

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train = x_train.reshape(60000, 784).astype('float32') / 255
x_test = x_test.reshape(10000, 784).astype('float32') / 255

model.compile(loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              optimizer=keras.optimizers.RMSprop())

model.summary() # This will throw an error as follows
# ValueError: This model has not yet been built. Build the model first by calling `build()` or calling `fit()` with some data, or specify an `input_shape` argument in the first layer(s) for automatic build.

# Need to run with real data to infer shape of different layers
history = model.fit(x_train, y_train,
                    batch_size=64,
                    epochs=1)

model.summary()
