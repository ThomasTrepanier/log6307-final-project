def is_correct_entry(idx, v):
    if idx % 2 == 0:
        return v == 'a'
    else:
        return v == 'b'

def my_fancy_test(l):
    return l and l[-1] == 'b' and all(is_correct_entry(idx, v) for idx, v in enumerate(l))
