from itertools import combinations, chain
from random import choice

teams = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
combo = list(combinations(teams, 2))

available = combo.copy()
rv = []

def random_pop(l):
    ch = choice(l)
    l.remove(ch)
    return ch

num_tries = 0

while True:
    num_tries += 1
    if num_tries > 99999:
        available = combo.copy()
        rv = []
        num_tries = 0

    l = [random_pop(available), random_pop(available), random_pop(available), random_pop(available), random_pop(available)]
    flat = list(chain.from_iterable(l))
    if len(set(flat)) == len(flat):
        #is unique
        rv.append(l)
    else:
        for i in l:
            available.append(i)
    if len(available) == 0:
        break

for l in rv:
    print(sorted(l))
