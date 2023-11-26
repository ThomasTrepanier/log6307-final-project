import pandas as pd

from itertools import groupby


def count_zeros(x):
    return [sum(1 for _ in group) for key, group in groupby(x, key=lambda i: i == 0) if key]


df = pd.DataFrame({'2010':[0, 45, 5], '2011': [12, 56, 0], '2012': [11, 22, 0], '2013': [0, 5, 0], '2014': [0, 0, 0]})

result = df.apply(count_zeros, axis=1)
print(result)
