import pandas as pd
import pyarrow as pa
import redis


r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)


def save_df_to_redis(r, redis_key, df):
    buffer = pa.serialize_pandas(df)
    r.set(redis_key, buffer.to_pybytes())


def load_df_from_redis(r, redis_key):
    buffer = r.get(redis_key)
    df = pa.deserialize_pandas(buffer)
    return df



data = {
    "Name": ["John", "Anna", "Peter"],
    "Age": [28, 24, 33],
}
df = pd.DataFrame(data)

save_df_to_redis(r, "key", df)
df_redis = load_df_from_redis(r, "key")
print(df_redis)
