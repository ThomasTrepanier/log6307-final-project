L = [[8100, 3], [8200, 5], [8400, 8]]

def newList(L):
    gen = []
    for subL in L:
        if len(gen) > 0:
            gen.append(gen[-1] + subL[1])
        else:
            gen.append(subL[1])

    for idx, subL in enumerate(L):
        subL[1] = gen[idx]

    print(L)

newList(L)
