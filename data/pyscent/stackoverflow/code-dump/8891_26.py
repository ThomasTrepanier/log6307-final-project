from pyspark.sql.dataframe import DataFrame
from functools import wraps

# Create a decorator to add a function to a python object
def add_attr(cls):
    def decorator(func):
        @wraps(func)
        def _wrapper(*args, **kwargs):
            f = func(*args, **kwargs)
            return f

        setattr(cls, func.__name__, _wrapper)
        return func

    return decorator

  
# Extensions to the Spark DataFrame class go here
def dataframe_extension(self):
  @add_attr(dataframe_extension)
  def drop_records():
    return(
      self
      .where(~((col('test1') == 'ABC') & (col('test2') =='XYZ')))
      .where(~col('test1').isin(['AAA', 'BBB']))
    )
  return dataframe_extension

DataFrame.dataframe_extension = property(dataframe_extension)
