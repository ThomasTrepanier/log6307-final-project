def check_more_than_100(x):
    v = None
    try:
        v = int(x)
    except:
        pass
    if v is not None:
        return (v > 100)
    return (False)
    
df['age1'] = df['age1'].apply(lambda x : 'dead' if check_more_than_100(x) else x)
df['age2'] = df['age2'].apply(lambda x : 'dead' if check_more_than_100(x) else x)

df2['age1'] = df2['age1'].apply(lambda x : 'dead' if check_more_than_100(x) else x)
df2['age2'] = df2['age2'].apply(lambda x : 'dead' if check_more_than_100(x) else x)
