import pandas as pd
import numpy as np
raw_data = {'age1': [23,45,210],'age2': [10,20,150],'name': ['a','b','c']}
df = pd.DataFrame(raw_data, columns = ['age1','age2','name'])

raw_data = {'age1': [80,90,110],'age2': [70,120,90],'name': ['a','b','c']}
df2 = pd.DataFrame(raw_data, columns = ['age1','age2','name'])

col_list=['age1','age2']
df_list=[df,df2]

def dead(df_list, col_list):
    for df in df_list:
        for col in col_list:
            df[col] = np.where(df[col] >= 100, "dead", df[col])
    return df_list


df

dead([df], col_list)
