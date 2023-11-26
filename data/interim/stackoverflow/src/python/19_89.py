import numpy as np
import pandas as pd
from datetime import dt

def change(x):
    return x.date()

df['date_of_admission'] = df['date_of_admission'].apply(change)

df['age'] = df['date_of_admission'].subtract(df['DOB']).dt.days // 365
