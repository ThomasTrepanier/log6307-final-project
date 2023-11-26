def mysort_two(df1,df2):
    d  = dict(zip(df2['c1'],df2['v1'].rank()))
    o = pd.concat((df2,df1),keys=[1,2],names=['Key'])
    a = o.to_numpy()[np.lexsort((o['v2'],o.index.get_level_values('Key'),
                o['c1'].map(d)))]
    return pd.DataFrame(a,columns=df2.columns)

#Same can also be written as below:
# def mysort_two(df1,df2):
#     d  = dict(zip(df2['c1'],df2['v1'].rank()))
#     o = pd.concat((df2,df1))
#     a = o.to_numpy()[np.lexsort((o['v2']
#                 ,np.append(np.ones(len(df2)), np.ones(len(df1))*2),
#                 o['c1'].map(d)))]
#     return pd.DataFrame(a,columns=df2.columns)
