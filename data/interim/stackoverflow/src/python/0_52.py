import numpy as np
import pandas as pd

df = pd.DataFrame({'a':[1,2,3,4,5,6],
               'b':[7,8,9,10,11,12],
               'c':['q', 'q', 'q', 'q', 'w', 'w']
              })

def groupby_transform(df: pd.DataFrame, group_by_column: str, lambda_to_apply) -> np.array:
    """
    Groupby and transform. Returns a column for the original dataframe.
    :param df: Dataframe.
    :param group_by_column: Column(s) to group by.
    :param lambda_to_apply: Lambda.
    :return: Column to append to original dataframe.
    """
    df = df.reset_index(drop=True)  # Dataframe index is now strictly in order of the rows in the original dataframe.
    values = df.groupby(group_by_column).apply(lambda_to_apply)
    values.sort_index(level=1, inplace=True)  # Sorts result into order of original rows in dataframe (as groupby will undo that order when it groups).
    result = np.array(values)  # Sort rows into same order as original dataframe.
    if result.shape[0] == 1:  # e.g. if shape is (1,1003), make it (1003,).
        result = result[0]
    return result  # Return column.


df["result"] = groupby_transform(df, "c", lambda x: x["a"].shift(1) + x["b"].shift(1))
