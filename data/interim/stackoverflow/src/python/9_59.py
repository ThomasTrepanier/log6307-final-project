def binary_repr_ar_v2(A, W):
    mask = (((A[:,None] & (1 << np.arange(W-1,-1,-1)))!=0))
    out = np.full((len(A),W),48, dtype=np.uint8)
    out[mask] = 49
    return out.view('S'+str(W)).ravel()
