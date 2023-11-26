def to_explode(df, by):

    # Filter dtypes and split into column names and type description
    cols, dtypes = zip(*((c, t) for (c, t) in df.dtypes if c not in by))
    # Spark SQL supports only homogeneous columns
    assert len(set(dtypes)) == 1, "All columns have to be of the same type"

    # Create and explode an array of (column_name, column_value) structs
    kvs = explode(array([
      struct(lit(c).alias("CATEGORY"), col(c).alias("qty_on_hand")) for c in cols
    ])).alias("kvs")

    return df.select(by + [kvs]).select(by + ["kvs.CATEGORY", "kvs.qty_on_hand"])
