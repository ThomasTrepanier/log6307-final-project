def tuple_pop(t: tuple, idx: int) -> tuple:
    return (*t[:idx], *t[idx+1:])

print(tuple_pop((0,1, 2), 0))  # outputs (1, 2)
print(tuple_pop((0,1, 2), 1))  # outputs (0, 2)
print(tuple_pop((0,1, 2), 2))  # outputs (0, 1)
