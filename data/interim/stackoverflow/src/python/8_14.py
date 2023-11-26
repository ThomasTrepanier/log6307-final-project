outliers = []
def get_outlier(x):
    num = 3
    mean_ = np.mean(x)
    std_ = np.std(x)
    for y in x:
        z_score = (y - mean_) / std_
        if np.abs(z_score) > num:
            outliers.append(y)
    return get_outlier

detect_outliers = get_outlier(df['value'])
sorted(df['value'])
q1, q3 = np.percentile(df['value'], [25, 75])
iqr = q3 - q1
lb = q1 - (1.5 * iqr)
ub = q3 - (1.5 * iqr)

for i in range(len(df)):
    if ((df['value'][i] < lb) | (df['value'][i] > ub)):
        df['value'][i] = np.random.randint(1, 50)
