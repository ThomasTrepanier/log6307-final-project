import pandas as pd

def slice_df_by(df_, slice_by=["Oman", "Nairobi",], slice_idx='country'):
    idxn = df_.index.names.index(slice_idx)
    return df_.loc[tuple([slice(None)]*idxn +[slice_by] ), :]

gender = tuple(["male", "female"]*6)
thrown = tuple(["rock", "scissors", "paper"]*4) 
country = tuple(["Nairobi", "Oman", "Djibouti", "Belize"]*3) 
names = tuple(["Chris", "Pat", "Michele", "Thomy", "Musa", "Casey"]*2)

tuples = list(zip(gender, thrown, country, names))

idx = pd.MultiIndex.from_tuples(tuples, 
                                names=["gender", "thrown", "country", "name"])

df = pd.DataFrame({'Count A': [12., 70., 30., 20.]*3, 
                   'Count B': [12., 70., 30., 20.]*3}, index=idx)
