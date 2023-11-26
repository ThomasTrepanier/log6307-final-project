import pandas as pd
df = pd.DataFrame({'naics':['311', '311919', '3159', '331', '332', '332913']})

def str_replace2(df, s, col, term): 
    df.loc[s.astype(str).str[:2] == term, col] = term
    return df

df = str_replace2(df, df.naics, 'naics', '31')
