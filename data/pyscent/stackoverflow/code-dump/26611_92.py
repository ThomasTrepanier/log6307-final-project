dictionary = {'hello': 3 , 'world':{'this': 5 , 'is':{'a': 3, 'dict': None}}}

def get_dups(a, values=None):
    if values is None: values = []
    if (a in values): return True
    values.append(a)
    if type(a) == dict:
        for i in a.values():
            if (get_dups(i, values=values)):
                return True
    return False

print(get_dups(dictionary))
