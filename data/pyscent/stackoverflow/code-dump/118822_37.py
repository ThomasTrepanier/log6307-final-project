def start_over_18(p):
    it = iter(p)
    for x in it:
        if x > 18:
            return [x, *it]
    return []
