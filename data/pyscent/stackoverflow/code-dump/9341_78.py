def type_checker(data):
    return (
        isinstance(data, list)
        and all(isinstance(x, dict) for x in list)
        and all(isinstance(k, str) and isinstance(v, int) for x in list for k, v in x.items())
    )
