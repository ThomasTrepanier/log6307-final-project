def fn(n):
    def _fn(n, calls):
        if n <= 1:
            return n, calls
        # n > 1 is a given by this point.
        return _fn(n / 2 if n % 2 == 0 else 3 * n + 1, calls + 1)

    return _fn(n, 1)
