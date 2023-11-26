# `splits` is a list of the number of records you want in each output file
def split_files(filename: str, splits: List[int]) -> None:
    dataset: tf.data.Dataset = tf.data.TFRecordDataset(filename)
    rec_counter: int = 0

    # An extra iteration over the data to get the size
    total_records: int = len([r for r in dataset])
    print(f"Found {total_records} records in source file.")

    if sum(splits) != total_records:
        raise ValueError(f"Sum of splits {sum(splits)} does not equal "
                         f"total number of records {total_records}")

    rec_iter:Iterator = iter(dataset)
    split: int
    for split_idx, split in enumerate(splits):
        outfile: str = filename + f".{split_idx}-{split}"
        with tf.io.TFRecordWriter(outfile) as writer:
            for out_idx in range(split):
                rec: tf.Tensor = next(rec_iter, None)
                rec_counter +=1
                writer.write(rec.numpy())
        print(f"Finished writing {split} records to file {split_idx}")
