def iterator2dataframes(iterator, chunk_size: int):
  """Turn an iterator into multiple small pandas.DataFrame

  This is a balance between memory and efficiency
  """
  records = []
  frames = []
  for i, record in enumerate(iterator):
    records.append(record)
    if i % chunk_size == chunk_size - 1:
      frames.append(pd.DataFrame(records))
      records = []
  if records:
    frames.append(pd.DataFrame(records))
  return pd.concat(frames)

time_0 = time()
cursor = collection.find()
chunk_size = 1000
df = iterator2dataframes(cursor, chunk_size)
print("Reading database with chunksize = {} took {}".format(chunk_size,time()-time_0))
