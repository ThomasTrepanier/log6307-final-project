def exists_object(obj: str) -> bool: 
    """ 
    Checks whether there is an object of the given name in the environment.
    """

    # The environment grid is assumed to be a global variable named "environment"
    for row in environment:
        for cell in row:
            # The first character in the cell string represents the object
            if OBJECT_TO_STR[obj] == cell[0]:
                return True
    return False
