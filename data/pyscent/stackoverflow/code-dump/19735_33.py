def more_than_one(it):
    next(it)  # Assumes at least once, which is already the case with groupby groups
    try:
        next(it)
    except StopIteration:
        return True
    return False

outputlist = [x for x, grp in groupby(inputlist) if not more_than_one(grp)]
