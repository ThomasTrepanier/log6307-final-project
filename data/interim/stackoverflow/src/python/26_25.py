def select_and(df, cols, vals):
    res = pd.Series(True, dtype='bool', index=df.index)
    for col, val in zip(cols, vals):
        res = (res & (df[col] == val))
    return df[res]
