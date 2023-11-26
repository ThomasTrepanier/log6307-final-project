def pure_python(list_of_tuples):
    res = [tuple()]
    for lst in list_of_tuples:
        res += [(*r, x) for r in res for x in lst]
    return res


def with_itertools(list_of_tuples):
    set_combos = chain.from_iterable(combinations(list_of_tuples, i) for i in range(len(list_of_tuples) + 1))
    return list(chain.from_iterable(map(lambda x: product(*x), set_combos)))


assert sorted(with_itertools(blubb), key=str) == sorted(pure_python(blubb), key=str)
