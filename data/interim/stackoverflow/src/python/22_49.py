def find_sum(s, lst):
    indices = {x: i for i, x in enumerate(lst)}
    for i, x in enumerate(lst):
        target = s - x
        if x <= target and target in indices and i != indices[target]:
            yield x, target  # <- I also simplified this
