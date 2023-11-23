def exists_obj(grid: Grid, obj: str, col: str) -> bool:
    """ 
    Checks whether there is an object of the given name and color in the environment.
    """
    for row in range(grid.rows):
        for col in range(grid.cols):
            cell = grid.cells[row][col]
            if cell == OBJECT_TO_STR[obj] + COLOR_TO_STR[col]:
                return True
    return False

def get_position(grid: Grid, obj: str, col: str) -> Tuple[int, int]:
    """
    If there is an object of given name and color in the environment, return its (x,y) coordinate.
    Otherwise, return (-1, -1)
    """
    for row in range(grid.rows):
        for col in range(grid.cols):
            cell = grid.cells[row][col]
            if cell == OBJECT_TO_STR[obj] + COLOR_TO_STR[col]:
                return (row, col)
    return (-1, -1)

def get_agent_position(grid: Grid):
    """
    Return the position of the agent
    """
    for row in range(grid.rows):
        for col in range(grid.cols):
            cell = grid.cells[row][col]
            if cell[0] == '>':  # the agent is represented by '>'
                return (row, col)
    return (-1, -1)

def get_agent_direction(grid: Grid):
    """
    Return the direction the agent is facing
    """
    for row in range(grid.rows):
        for col in range(grid.cols):
            cell = grid.cells[row][col]
            if cell[0] == '>':
                return AGENT_DIR_TO_STR[0]  # right
            elif cell[0] == 'V':
                return AGENT_DIR_TO_STR[1]  # down
            elif cell[0] == '<':
                return AGENT_DIR_TO_STR[2]  # left
            elif cell[0] == '^':
                return AGENT_DIR_TO_STR[3]  # up
    return None
