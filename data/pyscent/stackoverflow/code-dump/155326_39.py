import perfplot
import pandas as pd
import numpy as np

def stack(df):
    df1 = df.stack().reset_index().drop(columns='level_1').drop_duplicates()

    df1['col'] = df1.groupby('level_0').cumcount()
    df1 = (df1.pivot(index='level_0', columns='col', values=0)
              .rename_axis(index=None, columns=None))
    return df1

def apply_drop_dup(df):
    return pd.DataFrame.from_dict(df.apply(lambda x: x.drop_duplicates().tolist(),
                                           axis=1).to_dict(), orient='index')

def apply_unique(df):
    return pd.DataFrame(df.apply(pd.Series.unique, axis=1).tolist())


def list_map(df):
    return pd.DataFrame(list(map(pd.unique, df.values)))


perfplot.show(
    setup=lambda n: pd.DataFrame(np.random.choice(list('ABCD'), (n, 4)),
                                 columns=list('abcd')), 
    kernels=[
        lambda df: stack(df),
        lambda df: apply_drop_dup(df),
        lambda df: apply_unique(df),
        lambda df: list_map(df),
    ],
    labels=['stack', 'apply_drop_dup', 'apply_unique', 'list_map'],
    n_range=[2 ** k for k in range(18)],
    equality_check=lambda x,y: x.compare(y).empty,  
    xlabel='~len(df)'
)
