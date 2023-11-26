def bresenham(p_1, p_2):
    dx = p_2.x - p_1.x
    dy = p_2.y - p_1.y

    x = p_1.x
    y = p_1.y
    plot_point(x, y)  # Replace this line with your own drawing logic

    idk = abs(dy) - abs(dx) / 2  # Corrected error term calculation

    while x < p_2.x:
        x += 1
        if idk < 0:
            idk += abs(dy)
        else:
            y += 1 if dy > 0 else -1
            idk += abs(dy) - abs(dx)
        plot_point(x, y)  # Replace this line with your own drawing logic
