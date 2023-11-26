# make it a generator
def _rng():
    while True:
        yield np.random.randint(2,20)//2

# a non-random number generator
def _nrng():
    numbers = np.arange(1,10.5,0.5)
    for i in range(len(numbers)):
        yield numbers[i]

rng = _rng()
nrng = _nrng()
for j in range(10):
    print('random number', next(rng))
    print('non-random number', next(nrng))
