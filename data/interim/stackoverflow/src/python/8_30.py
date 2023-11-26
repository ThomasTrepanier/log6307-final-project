def overlaps(ranges):
    ranges = sorted(ranges)  # If our inputs are garunteed sorted, we can skip this
    it = iter(ranges)
    try:
        curr_start, curr_stop = next(it)
        # overlaps = False  # If we want to exclude output ranges not produced by overlapping input ranges
    except StopIteration:
        return
    for start, stop in it:
        if curr_start <= start <= curr_stop:  # Assumes intervals are closed
            curr_stop = max(curr_stop, stop)
            # overlaps = True
        else:
            # if overlaps:
            yield curr_start, curr_stop
            curr_start, curr_stop = start, stop
            # overlaps = False
    # if overlaps:
    yield curr_start, curr_stop

print(list(overlaps([(1, 50), (49, 70), (75, 85), (84, 88), (87, 92)])))
# [(1, 70), (75, 92)]

print(list(overlaps([(20, 30), (5, 10), (1, 7), (12, 21)])))
# [(1, 10), (12, 30)]
