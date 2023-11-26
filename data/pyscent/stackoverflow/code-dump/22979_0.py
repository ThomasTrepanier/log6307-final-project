import numpy as np


def my_brand_new_generator(n, a=1, b=100):
    i = 0
    while i < n:
        x = np.random.randint(a, b)
        if x > 50:
            yield x
            i += 1


numbers = list(my_brand_new_generator(100))
print(numbers[10])
# [94 97 50 53 53 89 59 69 71 86]

print(len(numbers))
# 100
