@tf.function
def train_step(x_batch):
    with tf.GradientTape() as tape:
        loss = self.encoder_model.loss.compute_loss(x_batch)
    gradients = tape.gradient(loss, self.encoder_model.get_trainable_variables())
    self.optimizer.apply_gradients(zip(gradients, self.encoder_model.get_trainable_variables()))
