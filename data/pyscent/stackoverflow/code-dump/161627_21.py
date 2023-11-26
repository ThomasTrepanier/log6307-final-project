def find_duplicates(ls):
    if type(ls) != list:
        return -1   
    non_dupe = []
    i = 0
    while i < len(ls):
        if ls[i] < 1:
            return -1
        elif ls[i] in non_dupe:
            return ls[i]
        else:
            non_dupe.append(i)
        i += 1
    return 0
