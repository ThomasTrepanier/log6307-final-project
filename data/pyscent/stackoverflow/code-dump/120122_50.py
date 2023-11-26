def find_sum(s, lst):
    targets = set(lst)
    for x in targets:
        target = s - x
        if x < target and target in targets:
            yield x, target
