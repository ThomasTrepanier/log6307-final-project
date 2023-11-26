s = "year:2020,concepts:[ab553,cd779],publisher:elsevier"


def split_by_commas(s):
    lst = list()
    last_bracket = ''
    word = ""
    for c in s:
        if c == '[' or c == ']':
            last_bracket = c
        if c == ',' and last_bracket == ']':
            lst.append(word)
            word = ""
            continue
        elif c == ',' and last_bracket == '[':
            word += c
            continue
        elif c == ',':
            lst.append(word)
            word = ""
            continue
        word += c
    lst.append(word)
    return lst
main_lst = split_by_commas(s)

print(main_lst)
