import random
import numpy as np

def random_index_each(array):
    def random_index(item):
        return (item, random.choice(np.where(array == item)[0]))
    return dict(map(random_index, set(array)))

if __name__ == '__main__':
    array = np.array([2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 1, 1, 0, 1, 0, 0, 2, 2, 1])
    for _ in range(4):
        print(random_index_each(array))
