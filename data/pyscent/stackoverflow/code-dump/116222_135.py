num = [8, 9, 4, 1, 2, 3]

def con(rng, pos=0):
    if pos < len(rng):
        if (pos > 0 and rng[pos]-1 == rng[pos-1]) or (pos < len(rng) -1 and rng[pos]+1 == rng[pos+1]):
            print("con", rng[pos])
        con(rng, pos+1)

con(num)
