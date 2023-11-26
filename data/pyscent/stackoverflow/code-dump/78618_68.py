def my_mse_loss_b(b):
     def mseb(y_true, y_pred):
         ...
         a = np.ones_like(y_true) #numpy array here is not recommended
         return K.mean(K.square(y_pred - y_true)) + a
     return mseb
