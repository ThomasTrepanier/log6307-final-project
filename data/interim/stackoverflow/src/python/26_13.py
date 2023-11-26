import itertools

import numpy as np
import pandas as pd
from numpy import nan

df1 = pd.DataFrame({
    'c1': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'D', 'D', 'D'],
    'c2': ['P', 'T', 'Y', 'P', 'T', 'Y', 'P', 'T', 'Y', 'P', 'T', 'Y'],
    'v1': [4, 3, 2, 0, 2, 0, 1, 1, 1, 1, 2, 1],
    'v2': [1, 1, 0, 1, 2, 2, 2, 2, 1, 1, 0, 1]
})

df2 = pd.DataFrame({
    'c1': ['A', 'B', 'C', 'D'],
    'c2': [nan, nan, nan, nan],
    'v1': [9, 2, 3, 4],
    'v2': [2, 5, 5, 2]
})


def op_fn(df1, df2):
    result = []
    for i, row in df2.sort_values('v1').iterrows():
        result.append(row.to_frame().T)
        result.append(df1[df1['c1'].eq(row['c1'])].sort_values('v2'))
    return pd.concat(result, ignore_index=True)


def cat_ordered(df1, df2):
    # Establish ordering based on df2
    cat_type = pd.CategoricalDtype(df2.sort_values('v1')['c1'], ordered=True)
    return (
        # Add Indicator to each DataFrame
        pd.concat([df.assign(indicator=i) for (i, df) in enumerate([df1, df2])])
            # Set c1 to the categorical ordering from above
            .astype({'c1': cat_type})
            # Sort By Categorical, then df2 first then v2 within dfs
            .sort_values(['c1', 'indicator', 'v2'],
                         ascending=(True, False, True),
                         ignore_index=True)
            # Remove Indicator column
            .drop(columns='indicator')
    )


def groupby_fn(df1, df2):
    y = df1.assign(ind=df1['v1'])
    x = df2.groupby("c1").apply(
        lambda v: pd.concat(
            [y[y["c1"].eq(v["c1"].iat[0])], v.sort_values("v2")]
        )
    )
    x.loc[:, "ind"] = x.loc[:, "ind"].ffill()
    return x.sort_values("ind").drop(columns="ind").reset_index(drop=True)


def concat_itertools(df1, df2):
    out = pd.concat([df1.sort_values('v1'),
                     df2.sort_values('v2')],
                    ignore_index=True)
    return out.loc[itertools.chain.from_iterable(out.groupby('c1', sort=False)
                                                 .groups.values())]


def helpcol(df1, df2):
    cat_type = pd.CategoricalDtype(df2.sort_values('v1')['c1'], ordered=True)
    dfc = pd.concat([df1, df2])
    dfc["c2sort"] = dfc["c2"].notna()
    dfc["c1sort"] = dfc["c1"].astype(cat_type)
    return dfc.sort_values(["c1sort", "c2sort", "v2"], ignore_index=True).drop(
        ["c2sort", "c1sort"], axis=1
    )


def U11(df1, df2):
    df = pd.concat([df1, df2], ignore_index=True)
    return (
        df.reindex(
            df.sort_values('c1')
                .groupby('c1', as_index=False)['v1'].transform('min')
                .squeeze().sort_values().index
        ).reset_index(drop=True)
    )


def mysort_anky(df1, df2):
    d = dict(zip(df2['c1'], df2['v1'].rank()))
    o = pd.concat((df2, df1), keys=[1, 2], names=['Key'])

    return (o.assign(k=o['c1'].map(d)).sort_values(['k', 'Key', 'v2'])
                .loc[:, list(df1)])  # .reset_index(drop=True)


def mysort_two_anky(df1, df2):
    d = dict(zip(df2['c1'], df2['v1'].rank()))
    o = pd.concat((df2, df1), keys=[1, 2], names=['Key'])
    a = o.to_numpy()[np.lexsort((o['v2'], o.index.get_level_values('Key'),
                                 o['c1'].map(d)))]
    return pd.DataFrame(a, columns=df2.columns)
