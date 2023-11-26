import itertools as it


def solution(*iterables):
    iterators = [iter(i) for i in iterables]  # make sure we're operating on iterators
    heads = [next(i) for i in iterators]  # requires each of the iterables to be non-empty
    sentinel = object()
    iterators = [it.chain((head,), iterator, (sentinel,), it.repeat(head))
                 for iterator, head in zip(iterators, heads)]
    # Create a dedicated iterator object that will be consumed each time a 'sentinel' object is found.
    # For the sentinel corresponding to the last iterator in 'iterators' this will leak a StopIteration.
    running = it.repeat(None, len(iterators) - 1)
    iterators = [map(lambda x, h: next(running) or h if x is sentinel else x,  # StopIteration causes the map to stop iterating
                     iterator, it.repeat(head))
                 for iterator, head in zip(iterators, heads)]
    return zip(*iterators)
