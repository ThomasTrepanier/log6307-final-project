def fn_cat_onehot(df):

    """Generate onehoteencoded features for all categorical columns in df"""

    printmd(f"df shape: {df.shape}")

    # NaN handing
    nan_count = df.isna().sum().sum()
    if nan_count > 0:
        printmd(f"NaN = **{nan_count}** will be categorized under feature_nan columns")

    # generation
    from sklearn.preprocessing import OneHotEncoder

    model_oh = OneHotEncoder(handle_unknown="ignore", sparse=False)
    for c in df.select_dtypes("category").columns:
        printmd(f"Encoding **{c}**")  # which column
        matrix = model_oh.fit_transform(
            df[[c]]
        )  # get a matrix of new features and values
        names = model_oh.get_feature_names_out()  # get names for these features
        df_oh = pd.DataFrame(
            data=matrix, columns=names, index=df.index
        )  # create df of these new features
        display(df_oh.plot.hist())
        df = pd.concat([df, df_oh], axis=1)  # concat with existing df
        df.drop(
            c, axis=1, inplace=True
        )  # drop categorical column so that it is all numerical for modelling

    printmd(f"#### New df shape: **{df.shape}**")
    return df
