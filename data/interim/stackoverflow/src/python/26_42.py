def Alollz(df):
    idx = pd.MultiIndex.from_product([np.unique(df['ID']), 
                                      np.arange(df['year'].min(), df['year'].max()+1)],
                                     names=['ID', 'year'])
   
    df_b = pd.DataFrame({'number': 0}, index=idx)
    df_b.update(df.set_index(['ID', 'year']))
    
    m = (df_b.groupby(level=0)['number'].cummax().eq(1) 
         & df_b[::-1].groupby(level=0)['number'].cummax().eq(1))
    
    return df_b.loc[m].reset_index()
