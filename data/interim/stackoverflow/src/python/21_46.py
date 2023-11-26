def find_welfare_crook(f, g, h, i, j, k):
    """f, g, and h are "ascending functions," i.e.,
i <= j implies f[i] <= f[j] or, equivalently,
f[i] < f[j] implies i < j, and the same goes for g and h.
i, j, k define where to start the search in each list.
"""
    # This is an implementation of a solution to the Welfare Crook
    # problems presented in David Gries's book, The Science of Programming.
    # The surprising and beautiful thing is that the guard predicates are
    # so few and so simple.
    i , j , k = i , j , k
    while True:
        if f[i] < g[j]:
            i += 1
        elif g[j] < h[k]:
            j += 1
        elif h[k] < f[i]:
            k += 1
        else:
            break
    return (i,j,k)
    # The other remarkable thing is how the negation of the guard
    # predicates works out to be:  f[i] == g[j] and g[j] == c[k].
