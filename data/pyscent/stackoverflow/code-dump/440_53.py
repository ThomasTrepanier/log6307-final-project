@pd.api.extensions.register_dataframe_accessor("ex")
class GroupbyTransform:
    """
    Groupby and transform. Returns a column for the original dataframe.
    """
    def __init__(self, pandas_obj):
        self._validate(pandas_obj)
        self._obj = pandas_obj

    @staticmethod
    def _validate(obj):
        # TODO: Check that dataframe is sorted, throw if not.
        pass

    def groupby_transform(self, group_by_column: str, lambda_to_apply):
        """
        Groupby and transform. Returns a column for the original dataframe.
        :param df: Dataframe.
        :param group_by_column: Column(s) to group by.
        :param lambda_to_apply: Lambda.
        :return: Column to append to original dataframe.
        """
        df = self._obj.reset_index(drop=True)  # Dataframe index is now strictly in order of the rows in the original dataframe.
        values = df.groupby(group_by_column).apply(lambda_to_apply)
        values.sort_index(level=1, inplace=True)  # Sorts result into order of original rows in dataframe (as groupby will undo that order when it groups).
        result = np.array(values)
        if result.shape[0] == 1:  # e.g. if shape is (1,1003), make it (1003,).
            result = result[0]
        return result
