# d = dict()
class Round7FloatEncoder(json.JSONEncoder): 
    def iterencode(self, obj): 
        if isinstance(obj, float): 
            yield format(obj, '.7f')


with open('test.json', 'w') as f:
    json.dump(d, f, cls=Round7FloatEncoder)
