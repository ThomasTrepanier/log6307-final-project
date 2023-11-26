def insert(xs, n):
    """
    Finds first element in `xs` greater than `n` and returns an inserted element.
    `xs` is assumed to be a sorted list.
    """
    for i, x in enumerate(xs):
        if x > n:
            return xs[:i] + [n] + xs[i:]

    return xs + [n]

sorted_arr = reduce(insert, arr, [])
print(sorted_arr)
