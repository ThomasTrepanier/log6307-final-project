import pandas as pd
import glob

def readFiles(path):
    files = glob.glob(path)
    dfs = [] # an empty list to store the data frames
    for file in files:
        data = pd.read_json(file, lines=True) # read data frame from json file
        dfs.append(data) # append the data frame to the list

    df = pd.concat(dfs, ignore_index=True) # concatenate all the data frames in the list.
    return df
