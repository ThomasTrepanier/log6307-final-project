from functools import reduce


def seriesrun(x, n):

    return reduce(lambda c, i: c + x**i*(-1)**i , range(n + 1), 0)
