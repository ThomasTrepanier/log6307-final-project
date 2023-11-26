def is_same(df):
    # this method returns true if all types are same, else returns false
    no_of_types = len(df.dtypes.unique())
    is_same = no_of_types == 1
    return is_same

diff_types1 = pd.DataFrame({"a": [1,2,3], "b": [2,3,4], "c": ["A", "C", "E"]})
diff_types2 = pd.DataFrame({"a": [1,2,3], "b": [2.0,3.1,4.2], "c": [2, 4, 5]})
same_types = pd.DataFrame({"a": [1,2,3], "b": [2,3,4], "c": [2, 4, 5]})
same_types2 = pd.DataFrame({"a": ["A", "C", "E"], "b": ["A", "C", "E"], "c": ["A", "C", "E"]})

is_same(diff_types1)
# False

is_same(diff_types2)
# False

is_same(same_types1)
# True

is_same(same_types2)
# True
