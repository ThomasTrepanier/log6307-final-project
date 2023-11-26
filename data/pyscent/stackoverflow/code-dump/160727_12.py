import random

random_range = range(0,1000)
exclude = [5, 55, 555]

def generate(n:int, ran: range, exclude:list):
    exclusive_range = range(ran.start, ran.stop-len(exclude))
    randoms = []
    for i in range(n):
        r = random.choice(exclusive_range)
        if r in exclude:
            r = exclusive_range.stop + exclude.index(r)
        randoms.append(r)
    return randoms

x = generate(1000, random_range, exclude)
