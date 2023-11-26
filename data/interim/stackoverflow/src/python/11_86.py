from itertools import chain
rr = []
pp = [[7,9], [10, 11]]
# create a unique set of elements from the lists in pp
unique_items_in_pp = set(chain(*pp))

def in_pp(items):
    """Takes an iterable, returns bool, True if an element of iterable is in pp"""
    return set(items).isdisjoint(unique_items_in_pp)

# reject anything into rr if in the set
print(list(filter(rr_add, [[1,2], [3,4], [5,6], [7,8]])))
