def myzip(iterables):
    iterators = [iter(it) for it in iterables]
    while True:
        items = []
        for it in iterators:
            try:
                items.append(next(it))
            except StopIteration:
                for i, peeked in enumerate(items):
                    iterables[i] = itertools.chain([peeked], iterators[i])
                return
            else:
                yield tuple(items)

gens = [range(10), range(8)]
list(myzip(gens))
print(next(gens[0]))
