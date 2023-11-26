from skimage.util import view_as_windows

def keep_N_per_group_v4(a, N):
    m = np.r_[True,a[:-1]!=a[1:]]
    w = view_as_windows(m,N)
    idx = np.flatnonzero(m)
    v = idx<len(w)
    w[idx[v]] = 1
    if v.all()==0:
        m[idx[v.argmin()]:] = 1
    return a[m]
