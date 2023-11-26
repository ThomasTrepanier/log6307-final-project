def get_numbers_in_between(li, x, y):
    mx, mn = sorted((x, y))
    return [n for n in li if mx <= n <= mn]

print(get_numbers_in_between(li=[9, 10, 11, 15, 19, 20, 21], x=20, y=10))
