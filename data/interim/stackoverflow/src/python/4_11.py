import pandas as pd


def my_append(self, x, ignore_index=False):
    if ignore_index:
        return pd.concat([self, x])
    else:
        return pd.concat([self, x]).reset_index(drop=True)


if not hasattr(pd.DataFrame, "append"):
    setattr(pd.DataFrame, "append", my_append)

