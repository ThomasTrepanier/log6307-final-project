def random_list(amount, minval, maxval, none_rate):
    from random import choice
    from numpy import linspace
    arr = linspace(minval, maxval, amount)
    none_count = round(float(amount * none_rate))
    rep = []
    col = [d for d in range(amount)]
    while none_count > 0:
        gen = choice(col)
        if gen not in rep:
            arr[gen] = None
            none_count -= 1
            rep.append(gen)
    return arr


print(random_list(10, 0, 100, 0.3))
