# decorator to attach a function to an attribute
def add_attr(cls):
    def decorator(func):
        @wraps(func)
        def _wrapper(*args, **kwargs):
            f = func(*args, **kwargs)
            return f

        setattr(cls, func.__name__, _wrapper)
        return func

    return decorator

# custom functions
def custom(self):
    @add_attr(custom)
    def add_column3():
        return self.withColumn("col3", lit(3))

    @add_attr(custom)
    def add_column4():
        return self.withColumn("col4", lit(4))

    return custom

# add new property to the Class pyspark.sql.DataFrame
DataFrame.custom = property(custom)

# use it
df.custom.add_column3().show()
