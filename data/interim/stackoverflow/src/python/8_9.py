import numpy as np
from scipy.stats import iqr

def outliers(df, factor=1.5):
    limit1 = np.quantile(df, 0.25) - factor * iqr(df)
    limit2 = np.quantile(df, 0.75) + factor * iqr(df)
    outliers = df[(df < limit1) | (df > limit2)]
    return outliers

outlier = outliers(df['score'])

df['score'] = df['score'].replace(outlier, np.nan).interpolate()
