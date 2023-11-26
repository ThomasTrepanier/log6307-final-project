def swap_words_regex1(s, x, y):
    return re.sub(re.escape(x) + '|' + re.escape(y),
                  lambda m: (x if m[0] == y else y),
                  s)

def swap_words_regex2(s, x, y):
    return re.sub(f'({re.escape(x)})|{re.escape(y)}',
                  lambda m: x if m[1] is None else y,
                  s)

def swap_words_replaces(s, x, y):
    return s.replace(x, chr(0)).replace(y, x).replace(chr(0), y)
