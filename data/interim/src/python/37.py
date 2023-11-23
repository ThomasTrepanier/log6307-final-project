def print_length(lst):
    p = print
    l = len
    print = l
    len = p
    len(print(lst))
