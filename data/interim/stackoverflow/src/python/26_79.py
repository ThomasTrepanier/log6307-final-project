def snail_arr(array):
    # compute the array size
    array_size = len(array) * len(array[0])

    # surround the array of '*'
    array = [['*' for _ in range(len(array[0]) + 2)]] + [
        ['*'] + array[i] + ['*']
        for i in range(len(array))
    ] + [['*' for _ in range(len(array[0]) + 2)]]

    # initialize position and direction
    position = 1, 1
    direction = RIGHT

    result = [get_value(array, position)]
    set_as_visited(array, position)
    nb_visited = 1

    while nb_visited < array_size:
        new_position = update_position(position, direction)
        if not is_visited(array, new_position):
            result += [get_value(array, new_position)]
            set_as_visited(array, new_position)
            position = new_position
            nb_visited += 1
        else:
            direction = next_direction(direction)
    return result
