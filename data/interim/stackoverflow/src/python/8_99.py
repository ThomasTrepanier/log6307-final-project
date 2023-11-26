def funcc(x, **kwargs):
    locals().update(kwargs)
    print(x, a, b, c, d)

kwargs = {'a' : 1, 'b' : 2, 'c':1, 'd': 1}
x = 1

funcc(x, **kwargs)
