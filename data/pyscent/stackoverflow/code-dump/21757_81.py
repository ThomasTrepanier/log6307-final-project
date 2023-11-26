@numba.jit(nopython=True)
def enum_bins_numba(ints):
    bins = numba.typed.List()
    for i in range(ints.max() + 1):
        inner = numba.typed.List()
        inner.append(0)  # An awkward way of forcing type inference.
        inner.pop()
        bins.append(inner)

    for x, i in enumerate(ints):
        bins[i].append(x)

    return bins
