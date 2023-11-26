import random

def get_data(n=1000):
    f = lambda n: random.randint(0, n)
    return [(f(n // 30), f(n // 20), f(n // 10)) for _ in range(n)]

def dissimilar(t1, t2):
    a, b, c = t1
    x, y, z = t2
    return (a != x) + (b != y) + (c != z)

def mst_score(data):
    dist = dict.fromkeys(data, 3)
    dist[data[0]] = 0
    score = 0
    while dist:
        one = min(dist, key=dist.get)
        score += dist.pop(one)
        for other in dist:
            dist[other] = min(dist[other], dissimilar(one, other))
    return score

total = 0
for i in range(100):
    data = get_data()
    score = mst_score(data)
    total += score
    print(score, total)
