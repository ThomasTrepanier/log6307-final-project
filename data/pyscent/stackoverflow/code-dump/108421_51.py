def intersection(seqs):
    seq = min(seqs, key=len)
    if not seq:
        return
    pivot = seq[len(seq) // 2]
    lows, counts, highs = [], [], []
    for seq in seqs:
        start = bisect.bisect_left(seq, pivot)
        stop = bisect.bisect_right(seq, pivot, start)
        lows.append(seq[:start])
        counts.append(stop - start)
        highs.append(seq[stop:])
    yield from intersection(lows)
    yield from itertools.repeat(pivot, min(counts))
    yield from intersection(highs)
