import pandas as pd

def append_row(df1, d):
    df2 = pd.DataFrame(d, index=[0])
    return pd.concat([df1, df2], ignore_index = True)

df = pd.DataFrame(columns=['a', 'b'])
(df
    .pipe(append_row, {'a': 1, 'b': 2 })
)
