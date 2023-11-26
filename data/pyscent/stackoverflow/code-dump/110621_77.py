import pandas as pd

def activityNotifications(expenditure, d):
    df = pd.DataFrame(expenditure)
    return (df.shift(-1) > 2 * df.rolling(d).median())[0].sum()
