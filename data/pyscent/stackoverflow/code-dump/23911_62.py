from random import randint, sample

def pseudo_rand_dict(n):
    d = dict()
    r = randint(n, n ** n)
    for i in range(n):
        d[f'key_{i}'] = r
    to_change = sample(d.keys(), 1)[0]
    d[to_change] = randint(n, n * r)
    return d

d = pseudo_rand_dict(5)

print(d)

{'key_0': 2523, 'key_1': 2523, 'key_2': 2523, 'key_3': 9718, 'key_4': 2523}
