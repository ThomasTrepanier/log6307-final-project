class Duplicated(ValueError): pass

def is_dup(d):
    values = set()
    def add(v):
        if isinstance(v, dict):
            map(add, v.values())
        else:
            if v in values:
                raise Duplicated
            else:
                values.add(v)
    try:
        add(d)
        return False
    except Duplicated:
        return True
