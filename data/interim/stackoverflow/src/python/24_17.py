class User(object):
    def __new__(cls, *args, **kwargs):
        # do some logic with the initial parameters

        return super().__new__(cls)
