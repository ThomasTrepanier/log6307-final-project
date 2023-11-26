def to_shape(a, shape):
    z = np.zeros(shape)
    z[:a.shape[0], :a.shape[1]] = a
    return z

