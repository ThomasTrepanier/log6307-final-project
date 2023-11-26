import pandas as pd

df = pd.read_csv('myfile', sep='=', header=None)
#        0  1
# 0   name  1
# 1  grade  A
# 2  class  B
# 3   name  2
# 4  grade  D
# 5  class  A

df = df.pivot(index=df.index // len(df[0].unique()), columns=0)
#       1           
# 0 class grade name
# 0     B     A    1
# 1     A     D    2
