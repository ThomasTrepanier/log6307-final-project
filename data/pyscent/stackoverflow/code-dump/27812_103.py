class Count:
    def __init__(self, num):
        self.str_num = iter(str(num))

    def __iter__(self):
        return self

    def __next__(self):
        c = next(self.str_num)
        return c in '02468'
