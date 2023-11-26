def save_model_checkpoint(epoch, logs):
    if logs['val_loss'] < save_model_checkpoint.best_val_loss:
        save_model_checkpoint.best_val_loss = logs['val_loss']
        model.save_weights(new_base_dir / 'model_checkpoint')
        print('Model checkpoint saved.')

save_model_checkpoint.best_val_loss = float('inf')

# Initialize your model here

model.fit(
    # Other model.fit arguments...
    callbacks=[tf.keras.callbacks.LambdaCallback(on_epoch_end=save_model_checkpoint)]
 )
