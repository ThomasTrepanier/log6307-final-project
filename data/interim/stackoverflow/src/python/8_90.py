def remove_symm_pairs(df):
    a = df.to_numpy(copy=False)
    b = np.sort(a,axis=1)
    idx = np.ravel_multi_index(b.T,(b.max(0)+1))
    sidx = idx.argsort(kind='mergesort')
    p = idx[sidx]
    m = np.r_[True,p[:-1]!=p[1:]]
    a_out = a[np.sort(sidx[m])]
    df_out = pd.DataFrame(a_out)
    return df_out
