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

client = MongoClient(host,port)
collection = client[db_name][collection_name]
cursor = collection.find()

df = iterator2dataframes(cursor, 1000)
