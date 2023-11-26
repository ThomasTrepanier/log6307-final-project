def combine_aggregates(df):
    #if type(grdf) == pd.core.frame.DataFrame:
    df1 = df
    result1 = df.sum(axis=1).rename(str(df1.index.names)).to_frame()
    df2 = df1.unstack()
    result2 = df2.sum(axis=1).rename(str(df2.index.names)).to_frame()
    df3 = df2.unstack()
    result3 = df3.sum(axis=1).rename(str(df3.index.names)).to_frame()
    df4 = df3.unstack()
    result4 = df4.sum(axis=1).rename(str(df4.index.names)).to_frame()

    return result1.append(result2).append(result3).append(result4)



combine_aggregates(grdf)     
