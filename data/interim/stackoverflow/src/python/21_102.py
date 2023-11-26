def split(seq, sep):
    start, stop = 0, -1
    while start < len(seq):
        try:
            stop = seq.index(sep, start)
        except ValueError:
            yield seq[start:]
            break
        yield seq[start:stop]
        start = stop + 1
    else:
        if stop == len(seq) - 1:
            yield []
