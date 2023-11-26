newdf = pd.DataFrame(columns=df.columns)
cols = list('QRST')
aggCol = 'P'
def aggregation(cols, origcols, aggCol, df, count=1):
    global newdf
    cols = origcols[:count]
    count += 1
    newdf = newdf.append(df.groupby(cols)[aggCol].agg('mean').round(2).reset_index().T.reindex(origcols + [aggCol]).T, ignore_index=True)
    if cols != origcols:
        aggregation(cols, origcols, aggCol, df, count)

aggregation(cols, cols, aggCol, df)
newdf['agg'] = newdf.pop(aggCol)
print(newdf)
