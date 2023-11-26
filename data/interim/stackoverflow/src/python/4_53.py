def openRedisCon():
   pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, db=0)
   r = redis.Redis(connection_pool=pool)
   return r

def storeDFInRedis(alias, df):
    """Store the dataframe object in Redis
    """

    buffer = io.BytesIO()
    df.to_parquet(buffer, compression='gzip')
    buffer.seek(0) # re-set the pointer to the beginning after reading
    r = openRedisCon()
    res = r.set(alias,buffer.read())

def loadDFFromRedis(alias, useStale: bool = False):
    """Load the named key from Redis into a DataFrame and return the DF object
    """

    r = openRedisCon()

    try:
        buffer = io.BytesIO(r.get(alias))
        buffer.seek(0)
        df = pd.read_parquet(buffer)
        return df
    except:
        return None


