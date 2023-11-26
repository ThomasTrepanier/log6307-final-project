def has_dupes(d):
    def values(d):
        seen = set()
        for k, v in d.items():
            if isinstance(v, dict):
                s = values(v)
                if seen & s:
                    raise RuntimeError()
                seen.update(s)
            else:
                if v in seen:
                    raise RuntimeError()
                seen.add(v)
        return seen
    try:
        values(d)
    except RuntimeError:
        return True
    return False
