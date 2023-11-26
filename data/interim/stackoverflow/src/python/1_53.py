list_of_dicts = [{'a': 1, 'b': 2}, {'c': 3}, {'d': 4}]

def merge(*dicts):    
    return dict( j for i in dicts[0] for j in i.items())

print(merge(list_of_dicts)) 
