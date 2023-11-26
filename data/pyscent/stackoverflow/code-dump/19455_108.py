def reduce_mean(x):
    import tensorflow as tf
    return tf.reduce_mean(x, axis=1)

model = Sequential()
model.add(Embedding(vocab_size, 300, weights=[embedding_matrix], input_length=max_length, trainable=False))
model.add(Lambda(reduce_mean))
model.add(Dense(8, input_dim=4, activation='relu'))
model.add(Dense(3, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X_train_pad, y_train, batch_size=128, epochs=25, validation_data=(X_val_pad, y_val), verbose=2)
model.save('my_model.h5') 
