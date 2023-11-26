import numpy as np

def sample(nof_samples, min, max, sum):
    p = np.full(nof_samples, 1.0/np.float64(nof_samples)) # probabilities

    while True:
        q = np.random.multinomial(sum, p)
        if not np.any(q > max):
            if not np.any(q < min):
                return q

t = sample(15, 5, 20, 227)
print(t)

t = sample(15, 5, 20, 227)
print(t)

t = sample(15, 5, 20, 227)
print(t)
