from itertools import islice, tee

def zipped(gen1, gen2, pred=list):
    g11, g12 = tee(gen1)
    z = pred(zip(g11, gen2))

    return (islice(g12, len(z), None), gen2), z

gen1 = iter(range(10))
gen2 = iter(range(5))

(gen1, gen2), output = zipped(gen1, gen2)

print(output)
print(next(gen1))
# [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
# 5
