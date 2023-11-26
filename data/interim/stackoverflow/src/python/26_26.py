def OP_problem():
    for result in itertools.product(a+b, repeat=10):
        a_count = len(x for x in result if x in a)
        # the trick is that every element was either from a or b;
        # so "at least 3 a's and at least 3 b's" is equivalent to
        # "at least 3 a's and at most 7 a's".
        if 3 <= a_count <= 7:
            yield result
