class encoder(tf.keras.layers.Layer):

    def __init__(
        self,
        vocab_size, num_layers, units, d_model, num_heads, dropout,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.vocab_size = vocab_size
        self.num_layers = num_layers
        self.units = units
        self.d_model = d_model
        self.num_heads = num_heads
        self.dropout = dropout

    # Other methods etc.
