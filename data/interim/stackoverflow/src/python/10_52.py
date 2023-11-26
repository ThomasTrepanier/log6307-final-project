def f(s=None):
    string = "f"
    def ret(p=None):
        nonlocal string
        string += "o"
        return ret if not p else string + p
    return ret if not s else string + s
