from pandas.api.types import is_numeric_dtype
def is_int_or_float(df):
    # this method returns true if all types are numeric
    is_numeric_types = sum([is_numeric_dtype(x) for x in df])
    return is_numeric_types

diff_types1 = pd.DataFrame({"a": [1,2,3], "b": [2,3,4], "c": ["A", "C", "E"]})
diff_types2 = pd.DataFrame({"a": [1,2,3], "b": [2.0,3.1,4.2], "c": [2, 4, 5]})
same_types = pd.DataFrame({"a": [1,2.2,3], "b": [2,3,4], "c": [2, 4, 5]})
same_types2 = pd.DataFrame({"a": ["A", "C", "E"], "b": ["A", "C", "E"], "c": ["A", "C", "E"]})

print(is_same(diff_types1))
# False

print(is_same(diff_types2))
# False

print(is_same(same_types1))
# True

print(is_same(same_types2))
# True
