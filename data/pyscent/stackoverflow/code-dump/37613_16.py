class MyList(list):
    def __iter__(self):
        print(f'__iter__() called on {self!r}')
        return super().__iter__()
        
    def count(self, item):
        cnt = super().count(item)
        print(f'count({item!r}) called on {self!r}, result: {cnt}')
        return cnt
