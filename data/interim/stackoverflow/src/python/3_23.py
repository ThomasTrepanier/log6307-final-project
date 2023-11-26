def getDictColumn_df2(df, new_col_name="newcol"):
    df[new_col_name] = tuple(map(lambda row: row._asdict(), df.itertuples(index=False)))
    return df[[new_col_name]]

getDictColumn_df2(df)
