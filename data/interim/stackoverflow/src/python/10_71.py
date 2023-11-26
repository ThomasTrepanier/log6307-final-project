import numpy as np

l = [
    0, 15, 30, 45, 60,
    75, 90, 105, 120,
    135, 150, 165, 180,
    195, 210, 225, 240,
    255, 270, 285, 300,
    315, 330, 345,
]

def roll_n_reversed(l, i, n):
    return np.roll(l, -l.index(i)-1)[:-(n+1):-1]

roll_n_reversed(l, 90, 13)
