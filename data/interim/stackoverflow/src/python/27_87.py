from itertools import islice


def iterate(itr, upper=5):
    return islice(nub(itr), upper)
