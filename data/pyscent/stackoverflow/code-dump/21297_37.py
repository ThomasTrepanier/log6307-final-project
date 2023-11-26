def extract(df, year):
    min_year = df['Date'].min()
    return df.loc[df['Date']==year, df.columns[year+1 - min_year]]

extract(df, 2003)
# 0    5
# 1    2
# Name: b1, dtype: int64
