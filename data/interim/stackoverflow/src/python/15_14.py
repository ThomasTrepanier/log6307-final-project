def pt2iter(pt):
    yield pt.x
    yield pt.y

xs, ys = zip(*map(pt2iter, points))
