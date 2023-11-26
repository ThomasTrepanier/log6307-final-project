def mysort(df1,df2):
    d = dict(zip(df2['c1'],df2['v1'].rank()))
    o = pd.concat((df2,df1),keys=[1,2],names=['Key'])

    return (o.assign(k=o['c1'].map(d)).sort_values(['k','Key','v2'])
            .loc[:,list(df1)])#.reset_index(drop=True)
