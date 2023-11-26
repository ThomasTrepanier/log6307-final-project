import os
import hashlib
import tensorflow as tf
from tqdm import tqdm


def split_tfrecord(tfrecord_path, n_splits):
    dataset = tf.data.TFRecordDataset(tfrecord_path)
    outfiles=[]
    for n_split in range(n_splits):
        output_tfrecord_dir = f"{os.path.splitext(tfrecord_path)[0]}"
        if not os.path.exists(output_tfrecord_dir):
            os.makedirs(output_tfrecord_dir)
        output_tfrecord_path=os.path.join(output_tfrecord_dir, f"{n_split:03d}.tfrecord")
        out_f = tf.io.TFRecordWriter(output_tfrecord_path)
        outfiles.append(out_f)

    for record in tqdm(dataset):
        sample = tf.train.Example()
        record = record.numpy()
        sample.ParseFromString(record)

        idx = int(hashlib.sha1(record).hexdigest(),16) % n_splits
        outfiles[idx].write(example.SerializeToString())

    for file in outfiles:
        file.close()
