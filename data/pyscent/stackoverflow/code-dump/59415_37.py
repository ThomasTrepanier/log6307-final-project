def appendDictToDF(df,dictToAppend):
  df = pd.concat([df, pd.DataFrame.from_records([dictToAppend])])
  return df

# Creating an empty dataframe
df = pd.DataFrame(columns=['a', 'b'])

# Appending a row
df= appendDictToDF(df,{ 'a': 1, 'b': 2 })
