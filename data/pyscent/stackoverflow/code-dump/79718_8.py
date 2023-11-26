def cross_category_features(
    df: pd.DataFrame,
    cross: list[str],
    remove_originals: bool = True
) -> pd.DataFrame:
    """
    Add feature crosses to the  based on the columns in cross_cols.  The columns must have already been factorized / ordinal encoded.

    :param data: The data to add feature crosses to
    :param cross_cols: The columns to cross. Columns must be int categorical 0 to n-1
    :param remove_originals: If True, remove the original columns from the data

    :return: The data with the feature crosses added
    """
    def set_hot_index(row):
        hot_index = (row[cross] * offsets).sum()
        row[hot_index + org_col_len] = 1
        return row

    org_col_len = df.shape[1]
    str_values = [[col + str(val) for val in sorted(df[col].unique())]
                  for col in cross]
    cross_names = ["_".join(x) for x in product(*str_values)]

    cross_features = pd.DataFrame(
        data=np.zeros((df.shape[0], len(cross_names))),
        columns=cross_names,
        dtype="int64")
    df = pd.concat([df, cross_features], axis=1)
    
    max_vals = df[cross].max(axis=0) + 1
    offsets = [np.prod(max_vals[i+1:]) for i in range(len(max_vals))]
    df.apply(set_hot_index, axis=1)

    if remove_originals:
        df = df.drop(columns=cross)

    return df

