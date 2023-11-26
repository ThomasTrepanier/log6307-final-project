def bresenham(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    steep = dy > dx
    if steep:
        x0, y0 = y0, x0
        x1, y1 = y1, x1
        dx, dy = dy, dx
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0
    y = y0
    ystep = 1 if y0 < y1 else -1
    error = 0
    for x in range(x0, x1 + 1):
        if steep:
            yield (y, x)
        else:
            yield (x, y)
        error += dy
        if 2 * error >= dx:
            y += ystep
            error -= dx
