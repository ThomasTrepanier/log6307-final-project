def breakIntoList(inp):
    if not inp:
        return []

    sublist = [inp[0]]
    output = []
    for a in inp[1:]:
        if a > sublist[-1]:
            sublist.append(a)
        else:
            output.append(sublist);
            sublist = [a]


    output.append(sublist)
    return output



list = [1, 4, 1, 2, 4, 3, 5, 4, 0]
print(list)
print(breakIntoList(list))
