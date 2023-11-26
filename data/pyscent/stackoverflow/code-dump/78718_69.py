def my_mse_loss_b(b):
     def mseb(y_true, y_pred):
         ...
         a = K.ones_like(y_true) #use Keras instead so they are all symbolic
         return K.mean(K.square(y_pred - y_true)) + a
     return mseb
