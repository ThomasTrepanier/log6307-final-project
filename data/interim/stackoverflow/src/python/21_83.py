def ceiling10(x):
    if (x > 10):
        return ceiling10(x / 10) * 10
    else:
        if (x <= 1):
            return ceiling10(10 * x) / 10
        else:
            return 10
for x in [1 / 1235, 0.5, 1, 3, 10, 125, 12345]:
    print(x, ceiling10(x))
