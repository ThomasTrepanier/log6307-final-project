import pandas as pd
a = [[1,2,3,4,5,6],[23,23,212,223,1,12]]
b = [1,1]


df = pd.DataFrame(zip(a,b), columns = ['a', 'b'])
def removing(row):
    val = [x for x in row['a'] if x != row['b']]
    return val
df['c'] = df.apply(removing,axis=1)
print(df)
