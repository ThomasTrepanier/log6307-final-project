from itertools import product, combinations

lst = [(1,2,3), (4,5,6), (7,8,9)]

def generate(lst):
    for idx in range(len(lst)):
        for val in lst[idx]:
            yield (val,)
            for j in range(1, len(lst)):
                for c in combinations(lst[idx+1:], j):
                    yield from tuple((val,) + i for i in product(*c))

l = [*generate(lst)]
print(l)
