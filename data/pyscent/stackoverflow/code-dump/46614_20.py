def A_Stefan_generator_stack3(m, n):
    def a(m):
        if not m:
            yield from count(1)
        x = 1
        for i, ai in enumerate(a(m-1)):
            if i == x:
                x = ai
                yield x
    return next(islice(a(m), n, None))
