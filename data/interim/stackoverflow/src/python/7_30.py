def digital_root(n):
    # convert to a string
    as_str = str(n)

    # get the value of the current first digit
    value = int(as_str[0])

    if len(as_str) > 1:
        # add the recursive return plus the value
        # for anything other than our base case.
        # pass the rest of the digits into our recursive call
        return digital_root(int(as_str[1:])) + value

    # our base case
    return value

print(digital_root(493193))
