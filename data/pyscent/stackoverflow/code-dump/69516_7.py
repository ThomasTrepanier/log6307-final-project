def path2wav(path):
    audio_raw = tf.io.read_file(path)
    return tf.audio.decode_wav(audio_raw)

dataset = tf.data.Dataset.list_files(PATH + "*.wav")
dataset = dataset.map(path2wav)
