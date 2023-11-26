import pyarrow as pa
import redis

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)

def storeInRedis(alias, df):
    df_compressed = pa.serialize(df).to_buffer().to_pybytes()
    res = r.set(alias,df_compressed)
    if res == True:
        print(f'{alias} cached')

def loadFromRedis(alias):
    data = r.get(alias)
    try:
        return pa.deserialize(data)
    except:
        print("No data")


storeInRedis('locations', locdf)

loadFromRedis('locations')
