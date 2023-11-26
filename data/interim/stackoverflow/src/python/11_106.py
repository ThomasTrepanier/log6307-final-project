def nth_most(str_in, n):
    c = collections.Counter(w.lower() for w in str_in.split())
    nth_occs = sorted(c.values())[-n]
    return [[k,v] for k,v in c.items() if v==nth_occs]

print(nth_most("apple apple apple call blue BlUe call woot",2))
