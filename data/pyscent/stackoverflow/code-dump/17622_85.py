def keep_N_per_group_v5(a, N):
    m = np.r_[True,a[:-1]!=a[1:]]
    w = view_as_windows(m,N)
    last_idx = len(a)-m[::-1].argmax()-1
    w[m[:-N+1]] = 1
    m[last_idx:last_idx+N] = 1
    return a[m]
