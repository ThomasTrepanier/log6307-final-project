df.reset_index(inplace=True)

def aggdata(x):
    if all([i <= 1 for i in x.count()]):
        return x.mean()
    else:
        raise ValueError

ddf = df.groupby('name').apply(aggdata)
