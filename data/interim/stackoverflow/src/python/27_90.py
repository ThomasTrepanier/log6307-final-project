def isplit_list(lst, v):
    while True:
        try:
            end = lst.index(v)
        except ValueError:
            break

        yield lst[:end]
        lst = lst[end+1:]

    if len(lst):
        yield lst


lst = ['a', 'k', 'b', 'c', 'k', 'd', 'e', 'g', 'k']

results = tuple(isplit_list(lst, 'k'))
