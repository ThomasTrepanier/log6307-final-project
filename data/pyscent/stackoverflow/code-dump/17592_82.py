from scipy.ndimage.morphology import binary_dilation

def keep_N_per_group(a, N):
    k = np.ones(N,dtype=bool)
    m = np.r_[True,a[:-1]!=a[1:]]
    return a[binary_dilation(m,k,origin=-(N//2))]
