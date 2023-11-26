def f(s, i, max_i, is_reversed):
    if i == max_i:
        return
    s += str(i)
    step = -1 if is_reversed else 1
    print(s[::step])
    is_reversed = not is_reversed
    i += 1
    f(s, i, max_i, is_reversed)

f('', 1, 10, False)
