import itertools

def find_sum(s, lst):
    return [x for x in itertools.combinations(lst, r=2) if x[0] + x[1] == s]

lst = [2, 4, 5, 6, 7, 8]
print(find_sum(12, lst))
