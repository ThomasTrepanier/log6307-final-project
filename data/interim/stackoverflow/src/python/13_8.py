import pandas as pd                                                                                                                                    
import numpy as np

raw_data = [
    ['Steve', 'Invalid Postcode', 'GBP', np.nan ],
    ['Robyn', 'Invalid Postcode', 'EUR', np.nan],
    ['James', 'Valid Postcode', 'GBP', 'GBR'],
    ['Halo', 'Invalid Postcode', 'EUR', np.nan],
    ['Jesus', 'Valid Postcode', 'GBP', 'GBR']
    ]

df = pd.DataFrame(columns=["Name", "PostCode", "Currency", "CountryISOCode"], data=raw_data)

def func(row):
    if row['CountryISOCode'] is np.nan and row['Currency'] == 'EUR':
        return 'IRE'
    elif row['CountryISOCode'] is np.nan and row['Currency'] == 'GBP':
        return 'GBR'
    else:
        return row['CountryISOCode']

df['CountryISOCode'] = df.apply(func, axis=1)

print(df)
