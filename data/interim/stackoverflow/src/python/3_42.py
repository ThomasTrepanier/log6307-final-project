import itertools

def combination(l):
    result = []
    for L in range(0, len(l)+1):
        for subset in itertools.combinations(l, L):
            result.append(list(subset))
    return result

print(combination([1, 2, 3]))
