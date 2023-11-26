def get_value(array, position):
    x, y = position
    return array[y][x]


def set_as_visited(array, position):
    x, y = position
    array[y][x] = '*'


def is_visited(array, position):
    return get_value(array, position) == '*'
