lst = [[1], [], [2], [], [3]]

def func(x):
    try:
        return x[0]
    except IndexError:
        return None

[func(i) for i in lst]
# [1, None, 2, None, 3]
