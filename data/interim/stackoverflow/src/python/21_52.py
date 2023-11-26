from heapq import merge
from itertools import groupby, chain

ls = [[1, 3, 5, 7], [1, 1, 3, 5, 7], [1, 4, 7, 9]]


def index_groups(lst):
    """[1, 1, 3, 5, 7] -> [(1, 0), (1, 1), (3, 0), (5, 0), (7, 0)]"""
    return chain.from_iterable(((e, i) for i, e in enumerate(group)) for k, group in groupby(lst))


iterables = (index_groups(li) for li in ls)
flat = merge(*iterables)
res = [k for (k, _), g in groupby(flat) if sum(1 for _ in g) == len(ls)]
print(res)
