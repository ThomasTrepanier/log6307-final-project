def f(g,a):
    ret = g.stack().reset_index(drop=True)
    ret.name = a
    return ret

pd.concat( (f(g,a) for a,g in df.groupby(df.columns.str[0], axis=1)), axis=1)
