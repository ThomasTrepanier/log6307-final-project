def newAvg(x):
    cm = x['count']*x['mean']
    sCount = x['count'].sum()
    sMean = cm.sum()
    return sMean/sCount
