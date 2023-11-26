def MaxMin(row):
    dfRange = df2[(df2['Date']>=row['From'])&(df2['Date']<=row['To'])] # df2 rows within a given date range
    row['High'] = dfRange['High'].max()
    row['Low'] = dfRange['Low'].min()
    return row

df1 = df1.apply(MaxMin, axis =1)
