import numpy as np
from itertools import groupby
from operator import itemgetter

def get_longest_consecutive_numbers(numbers):
    idx = max(
        (
            list(map(itemgetter(0), g)) 
            for i, g in groupby(enumerate(np.diff(numbers)==1), itemgetter(1)) 
            if i
        ), 
        key=len
    )
    return (idx[0], idx[-1]+1)

print(get_longest_consecutive_numbers(numbers))
#(4,6)
