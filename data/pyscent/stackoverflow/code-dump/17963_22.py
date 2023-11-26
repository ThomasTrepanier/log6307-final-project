import pandas as pd 
data = {'col1': ['cat', 'dog', 'mice'], 'col2' : ['black', 'white', 'grey'], 'col3' : ['small', 'medium', 'tinny'], 'col4': ['lovely','brave','fast']} 
df = pd.DataFrame(data) 

def getDictColumn_df1(df, new_col_name="newcol", cols_from_start=1):
    df[new_col_name] = tuple(map(lambda row: row._asdict(), df.iloc[:,cols_from_start:].itertuples()))
    return df[['col1', new_col_name]]

getDictColumn_df1(df)
