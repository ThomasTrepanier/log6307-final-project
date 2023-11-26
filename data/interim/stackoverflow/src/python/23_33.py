def nrng_gen():
    yield from range(10)

nrng = nrng_gen()

nrng_func = lambda: next(nrng)

for i in range(10):
    print(nrng_func())
