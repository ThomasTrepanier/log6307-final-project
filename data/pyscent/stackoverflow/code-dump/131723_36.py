import numpy as np
from functools import partial

# a random number generator
rng = lambda : np.random.randint(2,20)//2

# a non-random number generator
def nrng():
    numbers = np.arange(1,10.5,0.5)
    for i in range(len(numbers)):
        yield numbers[i]

def that_function(rng):
    print(*(rng() for j in range(10)))

that_function(rng)
that_function(nrng().__next__)
that_function(iter(np.arange(1,10.5,0.5)).__next__)
that_function(partial(next, nrng()))
