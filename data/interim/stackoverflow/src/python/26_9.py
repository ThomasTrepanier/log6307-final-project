a = [['1','2','3','a','b'],
     ['4','5','6','c','d'],
     ['7','8','9','e','f']]


pattern = ['4','5','6']

def find_index(data, pattern):
    for n, elt in enumerate(a):
        if elt[:3] == pattern:
            yield n

indices = find_index(a, pattern)
next(indices)
