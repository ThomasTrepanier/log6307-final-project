def split(seq, sep):
    seq, peek = iter(seq), sep
    while True:
        try:
            peek = next(seq)
        except StopIteration:
            break
        yield list(it.takewhile(sep.__ne__, it.chain((peek,), seq)))
    if peek == sep:
        yield []
