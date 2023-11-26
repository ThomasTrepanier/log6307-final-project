import more_itertools as mit


def sum_distrib(m, n):
    """Return an iterable of m items distributed across n spaces."""
    return [sum(x) for x in mit.distribute(n, [1]*m)]
