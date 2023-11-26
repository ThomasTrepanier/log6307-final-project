def funcc(refl):
    for i in range(len(refl)) - 1:
        if (refl[i + 1]) >= (refl[i]):
            return False
    return True
