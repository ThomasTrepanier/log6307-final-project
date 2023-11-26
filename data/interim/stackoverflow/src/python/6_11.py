import perfplot
import pandas as pd
import numpy as np

from collections import Counter
from itertools import chain

def counter(s):
    return pd.Series(Counter(chain.from_iterable(s)))

def explode(s):
    return s.explode().value_counts()

perfplot.show(
    setup=lambda n: pd.Series([['blue','green','brown'], [], ['green','red','blue']]*n), 
    kernels=[
        lambda s: counter(s),
        lambda s: explode(s),
    ],
    labels=['counter', 'explode'],
    n_range=[2 ** k for k in range(17)],
    equality_check=np.allclose,  
    xlabel='~len(s)'
)
