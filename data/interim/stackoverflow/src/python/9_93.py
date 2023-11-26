import numpy as np
import pandas as pd
import datetime as dtm

data = pd.read_csv("data.csv", parse_dates=["time"])

TIME_WINDOW = 5*60

def over_target_good(row, dataframe):
    time_window = dataframe.time <= (row.time
                                     + dtm.timedelta(seconds=TIME_WINDOW))
    window_data = dataframe[time_window]
    over_test = window_data.running_bid_max >= row.ask_price_target_good
    over_data = window_data[over_test]
    if len(over_data) > 0:
        return over_data.running_bid_max[over_data.index[0]]
    return np.NaN

def below_target_bad(row, dataframe):
    time_window = dataframe.time <= (row.time
                                     + dtm.timedelta(seconds=TIME_WINDOW))
    window_data = dataframe[time_window]
    below_test = window_data.running_bid_min <= row.ask_price_target_bad
    below_data = window_data[below_test]
    if len(below_data) > 0:
        return below_data.running_bid_min[below_data.index[0]]
    return np.NaN

print("OVER\n", data.apply(over_target_good, axis=1, args=(data,)) )
print("BELOW\n", data.apply(below_target_bad, axis=1, args=(data,)) )
