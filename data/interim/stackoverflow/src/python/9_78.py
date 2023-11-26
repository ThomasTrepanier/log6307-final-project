import itertools as it

def all_combinations(groups):
    result = set()
    for prod in it.product(*groups):
        for length in range(1, len(groups) + 1): 
            result.update(it.combinations(prod, length))
    return result

all_combinations([(1,2,3), (4,5,6), (7,8,9)])
