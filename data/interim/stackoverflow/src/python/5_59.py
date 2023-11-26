def model_map(row):
    if row['x'] >= max(df.maxValue_1, maxValue_2):
        return True
    else:
        return False
    
df['result'] = df.apply(lambda row : model_map(row), axis=1)
