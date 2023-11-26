RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3
NB_DIRECTIONS = 4


def next_direction(direction):
    return (direction + 1) % NB_DIRECTIONS


def update_position(position, direction):
    x, y = position
    if direction == RIGHT:
        return x + 1, y
    elif direction == DOWN:
        return x, y + 1
    elif direction == LEFT:
        return x - 1, y
    elif direction == UP:
        return x, y - 1

