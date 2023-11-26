import math


def get_powers(power, length):
    return [int(math.pow(power, x)) for x in range(1, length + 1)]


power_input = int(input('power:'))
length_input = int(input('length:'))

print(get_powers(power_input, length_input))
