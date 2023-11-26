def remover(row, replaces):
    for k,v in replacers.items():
        if k in row:
            row = row.replace(k, v)
    return row      


replacers = {',' : "",
         '.':'',
         '-':'',
         'ltd':'limited'
        }

for column in df.columns:
    df[column] = df[column].apply(lambda row: remover(row, replacers))
