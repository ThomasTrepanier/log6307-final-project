def helpcol(df1, df2):
    cat_type = pd.CategoricalDtype(df2.sort_values('v1')['c1'], ordered=True)
    dfc = pd.concat([df1, df2])
    dfc["c2sort"] = dfc["c2"].notna()
    dfc["c1sort"] = dfc["c1"].astype(cat_type)
    return dfc.sort_values(["c1sort", "c2sort", "v2"], ignore_index=True).drop(
        ["c2sort", "c1sort"], axis=1
    )
