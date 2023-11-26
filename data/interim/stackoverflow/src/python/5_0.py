def compare_ranges(x,y):
    return True if set(x) & set(y) else False

compare_ranges(range(1,100),range(110,150))
compare_ranges(range(1,100),range(90,150))
