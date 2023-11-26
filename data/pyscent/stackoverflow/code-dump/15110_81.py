def replace(lst, last=None):
    if lst:
        first, *rest = lst
        if first == "":
            for repl in replacements[last]:
                yield from replace(repl + rest)
        else:
            for res in replace(rest, first):
                yield [first] + res
    else:
        yield []

for l in lst:
    for x in replace(l):
        print(x)
