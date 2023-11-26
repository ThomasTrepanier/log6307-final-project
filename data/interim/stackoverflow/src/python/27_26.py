def compare_sign(s):
    if len(s) == 2:
        return s.iat[1] if s.iat[0] != s.iat[1] else 0
    else:
        return 0  # this case covers the first value in the rolling window series

def cross(df, field):
    return pd.Series([compare_sign(w) for w in df[field].apply(np.sign).rolling(2)])
