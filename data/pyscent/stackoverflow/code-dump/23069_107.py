def infinite_stream():
    """Yield a number from a (semi-)infinite iterator."""
    # Alternatively, `yield from itertools.count()`
    yield from iter(range(100000000))


# Helper
def get_data(iterable):
    """Print the state of `data` per stream."""
    return ", ".join([f"{x.__name__}: {x.data}" for x in iterable])
