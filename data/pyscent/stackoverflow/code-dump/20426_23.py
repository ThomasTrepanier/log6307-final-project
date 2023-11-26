def apply_union(x):
    ## join multiple columns to single sting in row
    x = x.apply(lambda row: ' '.join(row.values.astype(str)), axis=1)
    ## concat rows to single string
    x = x.str.cat(sep=" ")
    return x
df.groupby("Column1")[["Column2","Column3","Column4"]].apply(lambda x: apply_union(x))
