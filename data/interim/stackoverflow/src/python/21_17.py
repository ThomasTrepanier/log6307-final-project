# rename df columns by position (as opposed to index)
# mapper is a dict where keys = ordinal column position and vals = new titles
# unclear that using the native df rename() function produces the correct results when renaming by position
def rename_df_cols_by_position(df, mapper):
    new_cols = [df.columns[i] if i not in mapper.keys() else mapper[i] for i in range(0, len(df.columns))]
    df.columns = new_cols
    return
