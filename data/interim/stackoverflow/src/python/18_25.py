class ModelA(tf.keras.Model):
    # this model raises the error in the question
    __slots__ = ["model_layer"]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model_layer = layers.LayerNormalization()

    def call(self, inputs, training=None, mask=None):
        return self.model_layer(inputs)

    def get_config(self):
        return dict()


class ModelB(tf.keras.Model):
    # this model does NOT raise the error in the question
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model_layer = layers.LayerNormalization()

    def call(self, inputs, training=None, mask=None):
        return self.model_layer(inputs)

    def get_config(self):
        return dict()
