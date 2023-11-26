def loopy(series):
    series.copy()    # not necessary but just to make timings fair
    return pd.Series(
        (
            el.zfill(9) if len(el) < 9 else el.zfill(20)
            for el in series
        ),
        name=series.name,
    )

def str_accessor(series):
    target = series.copy()
    mask = series.str.len() < 9
    unmask = ~mask
    target[mask] = target[mask].str.zfill(9)
    target[unmask] = target[unmask].str.zfill(20)
    return target

def np_where_str_accessor(series):
    target = series.copy()
    return np.where(target.str.len()<9,target.str.zfill(9),target.str.zfill(20))

def fill_zeros(x, _len=len, _zfill=str.zfill):
    # len() and str.zfill() are cached as parameters for performance
    return _zfill(x, 9 if _len(x) < 9 else 20)

def apply_fill(series):
    series = series.copy()
    return series.apply(fill_zeros)

def cache_loopy(series, _len=len, _zfill=str.zfill):
    series.copy()
    return pd.Series(
      (_zfill(el, 9 if _len(el) < 9 else 20) for el in series), name=series.name)
