import pandas as pd
import pyarrow


def round_trip(fspec='/tmp/locations.parquet'):
    rows = [
        dict(lat=42.313, lng=-71.116),
        dict(lat=42.377, lng=-71.065),
        dict(lat=None, lng=None),
    ]

    df = pd.DataFrame(rows)
    df.to_parquet(fspec)
    del(df)

    df2 = pd.read_parquet(fspec)
    print(df2)


if __name__ == '__main__':
    round_trip()
