import pandas as pd
import numpy as np
import time
import math


# Method 1

def get_frame_method_1(l):

    list_example_d = {"time": l}

    df_1 = pd.DataFrame.from_dict(data=list_example_d, orient="columns")

    index_list = []

    for count, d in enumerate(df_1.time):
        index_list.extend(list(d.keys()))
        df_1.time[count]= list(d.values())[0]

    df_1.index= index_list

    return df_1


# Method 2

def get_frame_method_2(l):

    df_list = []

    for d in l:
        d_df = pd.DataFrame.from_dict(data=d, orient="index", columns=["time"])
        df_list.append(d_df)

    df_2 = pd.concat(df_list, axis= 0)

    return df_2


# Method 3

def get_frame_method_3(l):

    df_3 = (pd.concat(map(pd.Series, l))
            .to_frame('time')
        )
    
    return df_3


# Method 4

def get_frame_method_4(l):

    # build a nested dict from list_example and build df
    df_4 = pd.DataFrame.from_dict({k: {'time': v} for d in l for k,v in d.items()}, orient='index')

    return df_4


# Method 5

def get_frame_method_5(l):

    df_5 = pd.concat([ pd.Series(d.values(), index=d.keys())
        for d in l ]).to_frame('time')
    
    return df_4


check_length = 100000

list_example = []

for i in range(check_length):
    list_example.append({f"companies_info_{i}": i})


total_time_1_d = {}

for i in range(100):
    t_0 = time.time()
    df_1 = get_frame_method_1(list_example)
    t_1 = time.time()
    df_2 = get_frame_method_2(list_example)
    t_2 = time.time()
    df_3 = get_frame_method_3(list_example)
    t_3 = time.time()
    df_4 = get_frame_method_4(list_example)
    t_4 = time.time()
    df_5= get_frame_method_5(list_example)
    t_5 = time.time()
    total_time_1_d[f"{i}"] = {"Method 1": (t_1-t_0), "Method 2": (t_2-t_1), "Method 3": (t_3-t_2), "Method 4": (t_4-t_3), "Method 5": (t_5-t_4)}
    print(i)


total_time_df = pd.DataFrame.from_dict(data= total_time_1_d, orient="index")


for i in range(5):
    print(f"Method {i+1}: Mean - {total_time_df.describe().iloc[1, i]}, 95% CI ({total_time_df.describe().iloc[1, i]-1.96*(total_time_df.describe().iloc[2, i])/math.sqrt((total_time_df.describe().iloc[0, i]))}, {total_time_df.describe().iloc[1, i]+1.96*(total_time_df.describe().iloc[2, i])/math.sqrt((total_time_df.describe().iloc[0, i]))})")
