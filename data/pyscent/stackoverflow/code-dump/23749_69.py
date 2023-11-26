import numpy as np
import sys

def sample(nof_samples, min, max, sum):
    p = np.full(nof_samples, 1.0/np.float64(nof_samples)) # probabilities
    sum -= nof_samples * min
    max -= min
    if sum < 0 or sum > nof_samples * max:  # check that args have a feasible solutioon
        print('Inconceivable!')
        sys.exit()

    while True:
        q = np.random.multinomial(sum, p)
        if not np.any(q > max):
            return q + min

for _ in range(3):
    t = sample(15, 5, 20, 227)
    print(t)
    print(min(t), max(t), sum(t))  # confirm that all constraints have been met
