from random import randint

def partial_shuffle(l, factor=5):
    for _ in range(factor):
        a, b = randint(0, len(l)), randint(0, len(l)) # pick two random indexes
        l[b], l[a] = l[a], l[b] # swap the values at those indexes
    return l
