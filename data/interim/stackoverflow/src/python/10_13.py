import pandas as pd


def by_pandas(array, sep=' ', dtype=np.float):
    df = pd.DataFrame(array)
    return df[0].str.split(pat=sep, expand=True).to_numpy(dtype=dtype)
