@numba.jit(numba.void(numba.int64[:], 
                      numba.int64[:], 
                      numba.int64[:]), 
           nopython=True)
def enum_bins_numba_buffer_inner(ints, bins, starts):
    for x in range(len(ints)):
        i = ints[x]
        bins[starts[i]] = x
        starts[i] += 1

@numba.jit(nopython=False)  # Not 100% sure this does anything...
def enum_bins_numba_buffer(ints):
    ends = np.bincount(ints).cumsum()
    starts = np.empty(ends.shape, dtype=np.int64)
    starts[1:] = ends[:-1]
    starts[0] = 0

    bins = np.empty(ints.shape, dtype=np.int64)
    enum_bins_numba_buffer_inner(ints, bins, starts)

    starts[1:] = ends[:-1]
    starts[0] = 0
    return [bins[s:e] for s, e in zip(starts, ends)]
