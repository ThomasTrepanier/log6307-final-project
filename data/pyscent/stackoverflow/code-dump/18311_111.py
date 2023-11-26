def mask_nd(x, m):
    '''
    Mask a 2D array and preserve the
    dimension on the resulting array
    ----------
    x: np.array
       2D array on which to apply a mask
    m: np.array
        2D boolean mask  
    Returns
    -------
    List of arrays. Each array contains the
    elements from the rows in x once masked.
    If no elements in a row are selected the 
    corresponding array will be empty
    '''
    take = m.sum(axis=1)
    return np.split(x[m], np.cumsum(take)[:-1])
