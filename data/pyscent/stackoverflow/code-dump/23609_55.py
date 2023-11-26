def loopy(series):
    return pd.Series(
        (
            el.zfill(9) if len(el) < 9 else el.zfill(20)
            for el in series
        ),
        name=series.name,
    )

# to compare more fairly with the apply version
def cache_loopy(series, _len=len, _zfill=str.zfill):
    return pd.Series(
      (_zfill(el, 9 if _len(el) < 9 else 20) for el in series), name=series.name)
