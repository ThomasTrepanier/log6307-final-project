def finder(s, x, y):
    if len(x) == 0:
        return True
    elif len(s) < len(x):
        return False
    elif s[0] == x[0]:
        return finder(s[1:], x[1:], y)
    else:
        return finder(s[1:], y, y)
print(finder("1011101110", "111", "111"))
