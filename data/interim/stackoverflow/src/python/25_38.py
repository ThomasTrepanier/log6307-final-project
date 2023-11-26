import numpy as np
import tensorflow as tf

class cb_hold_best_weights(tf.keras.callbacks.Callback):
    best_weights = []
    def __init__(self):
        super(cb_hold_best_weights, self).__init__()
        self.best = np.Inf
    def on_epoch_end(self, epoch, logs=None):
        current_loss = logs.get('val_loss')
        if np.less(current_loss, self.best):
            self.best = current_loss
            cb_hold_best_weights.best_weights = self.model.get_weights()
            print('\nSaving weights validation loss= {0:6.4f}\n'.format(current_loss))
