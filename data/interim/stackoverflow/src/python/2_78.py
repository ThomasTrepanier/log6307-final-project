def zip_longest_special(*iterables):
    def filter(items, defaults):
        return tuple(d if i is sentinel else i for i, d in zip(items, defaults))
    sentinel = object()
    iterables = zip_longest(*iterables, fillvalue=sentinel)
    first = next(iterables)
    yield filter(first, [None] * len(first))
    for item in iterables:
        yield filter(item, first)
