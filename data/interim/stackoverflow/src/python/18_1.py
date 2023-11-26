from pyspark.sql import functions as F

def melt(df,cols,alias=('key','value')):
  other = [col for col in df.columns if col not in cols]
  for c in cols:
    df = df.withColumn(c, F.expr(f'map("{c}", cast({c} as double))'))
  df = df.withColumn('melted_cols', F.map_concat(*cols))
  return df.select(*other,F.explode('melted_cols').alias(*alias))
