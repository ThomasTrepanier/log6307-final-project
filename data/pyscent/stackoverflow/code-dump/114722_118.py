input_list = [1, 2, 3, 4, 5, 6]


def cyclic_perm(a):
    n = len(a)
    result = []
    for j in range(n):
        def f(l, k=j):
            return list(map(lambda i: l[i - k], range(n)))
        result.append(f)
    return result


for op in cyclic_perm(input_list):
    print(op(input_list))

