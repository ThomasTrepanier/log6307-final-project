def gen_factors_for(target, numbers):
    possible_j = set(numbers)
    limit = abs(target) ** 0.5
    for i in numbers:
        if abs(i) < limit and target % i == 0:
            j = target // i
            if j in possible_j and abs(j) > abs(i):
                yield i, j
