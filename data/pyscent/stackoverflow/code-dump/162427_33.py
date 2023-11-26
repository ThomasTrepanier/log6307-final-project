def map_randoms(df):
    df['col_rand'] = np.random.randint(0,2, size=len(df))
    return df

ddf = ddf.map_partitions(map_randoms)
ddf.persist()
