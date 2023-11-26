from itertools import chain

DEGREES = [
    0, 15, 30, 45, 60,
    75, 90, 105, 120,
    135, 150, 165, 180,
    195, 210, 225, 240,
    255, 270, 285, 300,
    315, 330, 345
]

def get_list_of_degrees(degree, resulting_list_length):
    index = DEGREES.index(degree)
    lower_index = index - (resulting_list_length)
    if index >= resulting_list_length:
        result = DEGREES[lower_index: index]  # start 12 values back, stop at index
    else:
        result = list(chain(DEGREES[lower_index:], DEGREES[:index])) # start 12 values back, stop at index
    return result

my_degrees = get_list_of_degrees(90, 12)
print(my_degrees)
