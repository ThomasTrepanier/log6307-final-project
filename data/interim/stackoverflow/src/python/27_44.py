def checkAB(s):

    # Check for the validity of the input
    if len(s) == 0 or s[0] != 'a':
        return False

    def loop(val):
        # Done processing, all is well
        if len(val) == 0:  
            return True

        # If the first char is a, recurse using the rest of the string
        if val[0] == 'a':
            return loop(val[1:])

        # If there are 3 chars, it can not be bbb
        if len(val) > 2 and val[0] == 'b' and val[1] == 'b' and val[2] == 'b':
            return False

        # If there is a single value left, and that is b it is not ok
        if len(val) == 1 and val[0] == 'b':
            return False

        # If we have bb, recurse using the rest of the string
        if val[0] == 'b' and val[1] == 'b':
            return loop(val[2:])

        # In any other case
        else:
            return False
    return loop(s)
