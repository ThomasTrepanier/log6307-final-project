import itertools

def factors(x, numbers):
    """ Generate all pairs in list of numbers that multiply to x.
    """
    for a, b in itertools.combinations(numbers, 2):
        if a * b == x:
            yield (a, b)

numbers = [2, 4, 5, 1, 6, 40, -1]
for pair in factors(20, numbers):
    print(pair)
