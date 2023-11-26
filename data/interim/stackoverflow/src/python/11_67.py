import os
import glob
import pandas as pd


def nested_files_to_df(path,ext): 

    paths = []
    all_data = pd.DataFrame()

    #--- Putting all files name  in one list ---#

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(tuple(ext)):
                s = os.path.join(root, file)
                paths.append(s)

    #--- Reading and merging all the  existing  excel files  into one  dataframe  ---#

    for f in paths:
        df = pd.read_excel(f)     
        all_data = all_data.append(df,ignore_index=True)

    return all_data
