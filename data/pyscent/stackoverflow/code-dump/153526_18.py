import time

u11time1 = time.time()

for i in range(5000):
    df = pd.read_clipboard()
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

u11time2 = time.time()

print('u11 time:', u11time2 - u11time1)

thepyguytime1 = time.time()

for i in range(5000):
    df = pd.read_clipboard()
    cols = list('QRST')
    aggCol = 'P'
    groupCols = []
    result = []
    for col in cols:
        groupCols.append(col)
        result.append(df.groupby(groupCols)[aggCol].agg(count='count').reset_index())
    result = pd.concat(result)[groupCols+['count']]

thepyguytime2 = time.time()

print('ThePyGuy time:', thepyguytime2 - thepyguytime1)
