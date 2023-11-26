class NumpyArray(list):
    def __getitem__(self, index):
        if isinstance(index, tuple) and len(index) == 2:
            return self[index[0]][index[1]]
        return super().__getitem__(index)

b = NumpyArray([[0, 1], [2, 3]])
b[1, 1]
