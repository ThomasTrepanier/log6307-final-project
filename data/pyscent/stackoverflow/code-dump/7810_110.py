def interperse(lst):
    for x, y in zip(lst, lst[1:]):
        yield ["V"] * (y[0] - x[-1] - 1)

groups = list(groupby_consecutive(lst))
print(list(interperse(groups)))
# [['V'], ['V', 'V'], ['V'], ['V', 'V'], ['V']]
