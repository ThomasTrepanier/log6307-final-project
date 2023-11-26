import pandas as pd
import random

def foo():
    df = pd.DataFrame()
    year = 2016
    names = ['Bill', 'Bob', 'Ryan']
    for day in range(1, 4, 1):
        for name in names:
            if random.choice([True, False]):   # sometimes a name will be missing
                continue
            value = random.randrange(0, 20, 1) # random value from heuristic
            col = '{}_{}'.format(year, day)    # column name
            new_df = pd.DataFrame({col: value, 'name':name}, index=[1]).set_index('name')
            df = pd.concat([df,new_df[~new_df.index.isin(df.index)].dropna()])
            df.update(new_df)
    #df.set_index('name', inplace=True, drop=True)
    print(df)
