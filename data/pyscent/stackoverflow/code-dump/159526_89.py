class MyDict(dict):
    def get(self, key, default=None, error=None):
        res = super().get(key,default)
        if res is None:
            if error == 'raise':
                raise SyntaxError()
            elif error == 'Exception':
                return SyntaxError()
        return res
