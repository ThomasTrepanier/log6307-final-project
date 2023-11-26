from pyspark.sql.types import BooleanType
from pyspark.sql import functions as F

def is_digit(val):
    if val:
        return val.isdigit()
    else:
        return False

is_digit_udf = udf(is_digit, BooleanType())

df = df.withColumn('Value', F.when(is_digit_udf(F.col('ID')), F.lit(True)).otherwise(F.lit(False)))
