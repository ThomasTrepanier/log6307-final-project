def getindex(l: list, element) -> int:
    for i, e in enumerate(l):
        if e == element:
            return i
    raise ValueError(f"{element} is not in list")
