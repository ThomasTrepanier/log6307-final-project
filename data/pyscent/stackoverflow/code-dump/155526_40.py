def with_numpy(df):
    arr = np.sort(df.to_numpy(), axis=1)
    r = np.roll(arr, 1, axis=1)
    r[:, 0] = np.NaN
    
    arr = np.where((arr != r), arr, np.NaN)
    
    # Move all NaN to the right. Credit @Divakar
    mask = pd.notnull(arr)
    justified_mask = np.flip(np.sort(mask, axis=1), 1)
    out = np.full(arr.shape, np.NaN, dtype=object) 
    out[justified_mask] = arr[mask]
    
    return pd.DataFrame(out, index=df.index).dropna(how='all', axis='columns')

with_numpy(df)
#   0  1    2    3
#0  A  B    C    D
#1  A  C    D  NaN
#2  B  C  NaN  NaN     # B/c this method sorts, B before C
#3  A  B  NaN  NaN
