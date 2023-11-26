def flip(a):

    #convert input string to list
    lst = list(a)

    #initialise output string
    out = ''

    # if more than 1 element is left, remove the first two elements and invert
    while len(lst)>1:
        a = lst.pop(0)
        b = lst.pop(0)
        out = out + b + a

    # if list has at least one element, add this one to the output string
    if lst:
        out = out + lst.pop()

    return out
