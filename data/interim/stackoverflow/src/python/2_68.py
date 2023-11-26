def none_replace(ls: list):
    prev, this = ls[0], None
    assert prev is not None, "First arg can't be None"

    for i in range(1, len(ls)):
        this = ls[i]
        if this is None:
            ls[i] = prev
        prev = this or ls[i]

    return ls

print('Replaced None List:', none_replace(['asd', None, None, 1, 2, None, None, 3, 4, None, 5, None, None]))
