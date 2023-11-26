def all_borders_zero(array):
    if not array.ndim:
        raise ValueError("0-dimensional arrays not supported")
    for dim in range(array.ndim):
        view = numpy.moveaxis(array, dim, 0)
        if not (view[0] == 0).all():
            return False
        if not (view[-1] == 0).all():
            return False
    return True
