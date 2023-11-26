from itertools import groupby
from operator import itemgetter

def groupby_consecutive(lst):
    for _, g in groupby(enumerate(lst), lambda x: x[0] - x[1]):
        yield list(map(itemgetter(1), g))

sorted_ids = [1, 2, 4, 5, 8, 9, 10, 12, 13, 16, 17, 18, 20]
print(list(groupby_consecutive(lst=sorted_ids)))
# [[1, 2], [4, 5], [8, 9, 10], [12, 13], [16, 17, 18], [20]]
