import pandas as pd
import numpy as np
from random import choices, randrange
from simple_benchmark import benchmark

def randvalue(chars="0123456789", _c=choices, _r=randrange):
    return "".join(_c(chars, k=randrange(5, 30))).lstrip("0")

fns = [loopy, str_accessor, np_where_str_accessor, apply_fill, cache_loopy]
args = { 2**i: pd.Series([randvalue() for _ in range(2**i)]) for i in range(14, 21)}

b = benchmark(fns, args, 'Series Length')

b.plot()
