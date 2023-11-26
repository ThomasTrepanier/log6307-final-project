def myfunc_improved(sets: List[set]) -> set:
    sd = set()
    goners = set()
    for s in sets:
        sd ^= s - goners
        goners |= s - sd
    return sd
