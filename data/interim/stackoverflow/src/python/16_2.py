class StratifiedGroupShuffleSplit(StratifiedShuffleSplit):
    """
    Note there is an assumption that the samples in a same group have a same label.
    """
    def __init__(
        self, n_splits = 10, *, test_size = None, 
        train_size = None, random_state = None
    ):
        super().__init__(
            n_splits = n_splits,
            test_size = test_size,
            train_size = train_size,
            random_state = random_state,
        )
        self._default_test_size = 0.1

    def _iter_indices(self, X, y, groups = None):
        if groups is None:
            raise ValueError("The 'groups' parameter should not be None.")
        groups = check_array(groups, input_name = "groups", ensure_2d = False, dtype = None)
        classes, group_indices = np.unique(groups, return_inverse = True)
        stratify = np.array([y[indices[0]] for indices in group_indices])

        for group_train, group_test in super()._iter_indices(X = classes, y = stratify):
            # these are the indices of classes in the partition
            # invert them into data indices

            train = np.flatnonzero(np.in1d(group_indices, group_train))
            test = np.flatnonzero(np.in1d(group_indices, group_test))

            yield train, test
