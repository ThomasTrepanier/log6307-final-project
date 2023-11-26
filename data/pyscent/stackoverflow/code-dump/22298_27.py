def merge_range(rng):
    starts, ends = [], []   
    for i, (x, y) in enumerate(rng):
        if i > 0:
            if x<= ends[-1]:
                ends[-1] = y
                continue
        starts.append(x)
        ends.append(y)
    return list(zip(starts, ends))
