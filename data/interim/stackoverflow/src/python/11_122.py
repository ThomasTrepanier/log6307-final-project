def islandlen_perrow(df, trigger_val=0):
    a=df.values==trigger_val
    pad = np.zeros((a.shape[0],1),dtype=bool)
    mask = np.hstack((pad, a, pad))
    mask_step = mask[:,1:] != mask[:,:-1]
    idx = np.flatnonzero(mask_step)
    island_lens = idx[1::2] - idx[::2]
    n_islands_perrow = mask_step.sum(1)//2
    out = np.split(island_lens,n_islands_perrow[:-1].cumsum())
    return out
