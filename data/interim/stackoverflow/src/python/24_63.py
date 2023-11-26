from random import randrange

def partial_shuffle(l, factor=5):
    n = len(l)
    for _ in range(factor):
        a, b = randrange(n), randrange(n)
        l[b], l[a] = l[a], l[b]
