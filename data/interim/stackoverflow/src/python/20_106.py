def split_int(i):
    while True:
        i, r = divmod(i, 10)
        yield r
        if not i:
            break
