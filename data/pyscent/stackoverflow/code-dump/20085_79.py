class Gen:
    def __init__(self,iterable):
        self.d = iter(iterable)
        self.sentinel = object()
        self.prev = self.sentinel
    def __iter__(self):
        return self
    @property
    def last_val_consumed(self):
        if self.prev is None:
            raise StopIteration
        if self.prev == self.sentinel:
            raise ValueError('Nothing has been consumed')
        return self.prev
    def __next__(self):
        self.prev = next(self.d,None)
        if self.prev is None:
            raise StopIteration
        return self.prev
