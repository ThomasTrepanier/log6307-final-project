def closerab(l, a=0, b=1):
    l = np.asarray(l)
    boolarr = (np.abs(l - b) > np.abs(l - a))

    # returns two lists of indices, one for numbers closer to a and one for numbers closer to b
    return boolarr.nonzero()[0], (boolarr==0).nonzero()[0]
