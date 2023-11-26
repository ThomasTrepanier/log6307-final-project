class Foo:
    def __init__(self):
        self.name = 'Foo!'
        @property
        def inst_prop():
            return f'Retrieving {self.name}'
        self.inst_prop = inst_prop
