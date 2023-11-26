from random import randint


def roll_dice(n):
    return [randint(1, 6) for _ in range(n)]


print('You re-rolled some dice and the new values are:',
    ', '.join(map(str, roll_dice(5)))
)
