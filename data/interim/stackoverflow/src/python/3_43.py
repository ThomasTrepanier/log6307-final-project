def combinations(return_len, iterable):
    if not return_len:
        return [[]]
    if not iterable:
        return []

    head = [iterable[0]]
    tail = iterable[1:]
    new_comb = [head + list_ for list_ in combinations(return_len - 1, tail)]

    return new_comb + combinations(return_len, tail)


input_list = [1, 2, 3]
result = []

for n in range(0, len(input_list) + 1):
    for single_result in combinations(n, input_list):
        result.append(single_result)

print(result)
