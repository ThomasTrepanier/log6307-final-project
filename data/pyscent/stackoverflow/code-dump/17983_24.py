def filter(row):
  # Add other conditions and just return row accordingly
  if ((row.year != 1990) | (row.month != 7)):
    return True
  return False

mask = df.apply(filter,axis=1)
df[mask]
