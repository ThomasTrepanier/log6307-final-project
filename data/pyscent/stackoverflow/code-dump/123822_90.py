def batched(cursor, batch_size):
    batch = []
    for doc in cursor:
        batch.append(doc)
        if batch and not len(batch) % batch_size:
            yield batch
            batch = []

    if batch:   # last documents
        yield batch

df = pd.DataFrame()
for batch in batched(cursor, 10000):
    df = df.append(batch, ignore_index=True)
