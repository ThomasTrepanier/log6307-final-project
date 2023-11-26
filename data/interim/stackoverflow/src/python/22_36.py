def start_over_18(p):
    for x in p:
        if x > 18:
            return p[p.index(x):]
    return []
