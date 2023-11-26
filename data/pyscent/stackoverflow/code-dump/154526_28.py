from itertools import product, permutations

def permutem(l1, l2, min_num=3, length=10):
    for n in range(min_num, length - min_num + 1):
        a, b = n, length - n
        for result in permutations(product(l1, r=a), product(l2, r=b)):
            yield result
