from time import time 
import pandas as pd
from multiprocessing.pool import ThreadPool


start_time = time()

pool = ThreadPool(processes=3)

Primary_File = "//ServerA/Testing Folder File Open/Report.xlsx"
Secondary_File_1 = "//ServerA/Testing Folder File Open/Report2.csv"
Secondary_File_2 = "//ServerA/Testing Folder File Open/Report2.csv"


# Define a function for the thread
def import_xlsx(file_name):
    df_xlsx = pd.read_excel(file_name)
    # print(df_xlsx.head())
    return df_xlsx


def import_csv(file_name):
    df_csv = pd.read_csv(file_name)
    # print(df_csv.head())
    return df_csv

# Create two threads as follows

Primary_df = pool.apply_async(import_xlsx, (Primary_File, )).get() 
Secondary_1_df = pool.apply_async(import_csv, (Secondary_File_1, )).get() 
Secondary_2_df = pool.apply_async(import_csv, (Secondary_File_2, )).get() 

Secondary_df = Secondary_1_df.merge(Secondary_2_df, how='inner', on=['ID'])
end_time = time()
