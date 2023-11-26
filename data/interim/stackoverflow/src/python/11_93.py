import pandas as pd

def flatten_dict(d):
    df = pd.io.json.json_normalize(d, sep='_')
    return df.to_dict(orient='records')[0]

dictionary = {'hello': 3 , 'world':{'this': 5 , 'is':{'a': 3, 'dict': None}}}

dictionary = flatten_dict(dictionary)
print('flattend')
print(dictionary)

rev_dictionary = {}

for key, value in dictionary.items():
    rev_dictionary.setdefault(value, set()).add(key)

print('reversed')
print(rev_dictionary)

is_duplicate = False
for key, values in rev_dictionary.items():
    if len(values) > 1:
        is_duplicate = True
        break

print('is duplicate?', is_duplicate)
