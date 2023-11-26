from itertools import zip_longest

def zip_left(*iterables, fillvalue=None):
    SENTINEL = object()
    
    for first, *others in zip_longest(*iterables, fillvalue=SENTINEL):
        if first is SENTINEL:
            return
        others = [i if i is not SENTINEL else fillvalue for i in others]
        yield (first, *others)


print(list(zip_left(['a', 'b', 'c'], [1, 2])))
print(list(zip_left(['a', 'b'], [1, 2, 3])))
