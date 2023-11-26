#import numba

df['change'] = df['close'].diff()
df['gain'] = df.change.mask(df.change < 0, 0.0)
df['loss'] = -df.change.mask(df.change > 0, -0.0)

#@numba.jit
def rma(x, n):
    """Running moving average"""
    a = np.full_like(x, np.nan)
    a[n] = x[1:n+1].mean()
    for i in range(n+1, len(x)):
        a[i] = (a[i-1] * (n - 1) + x[i]) / n
    return a

df['avg_gain'] = rma(df.gain.to_numpy(), 14)
df['avg_loss'] = rma(df.loss.to_numpy(), 14)

df['rs'] = df.avg_gain / df.avg_loss
df['rsi'] = 100 - (100 / (1 + df.rs))
