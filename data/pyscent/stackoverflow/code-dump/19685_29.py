import pandas as pd
df = pd.DataFrame({'name': ['john', 'mary', 'joseph', 'maria', 'john', 'mary', 'joseph', 'maria'],
                   'age': [12, 13, 12, 14, 12, 13, 12, 14],
                   'sex': ['m', 'f','m', 'f', 'm', 'f','m', 'f']})

df.index = df.index + 1

df['label'] = pd.Series()
def create_label(data, each_row):
   i = 0
   j = 1
   while i <= len(data):
      data['label'][i: i + each_row] = 'label' + str(j)
      i += each_row
      j += 1
   return data

df_new = create_label(df, 2)
