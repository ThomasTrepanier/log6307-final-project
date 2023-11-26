def keep_N_per_group_v3(a, N):
    m = np.r_[True,a[:-1]!=a[1:],True]
    idx = np.flatnonzero(m)
    c = np.diff(idx)
    return np.repeat(a[idx[:-1]],np.minimum(c,N))
