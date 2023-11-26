def intersection(iterables):
    target, count = None, 0
    for it in itertools.cycle(map(iter, iterables)):
        for value in it:
            if count == 0 or value > target:
                target, count = value, 1
                break
            if value == target:
                count += 1
                break
        else:  # exhausted iterator
            return
        if count >= len(iterables):
            yield target
            count = 0
