class GetAndRaise:
    def __init__(self):
        self.dict = dict()
    def __getitem__(self, key):
        try:
            return self.dict[key]
        except ValueError:
            raise MyException
    def __setitem__(self, key, value):
        self.dict[key] = value
    def get(self, key):
        return self[key]
