class Test:

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f'entering {self.name}')

    def __exit__(self, exctype, excinst, exctb) -> bool:
        print(f'exiting {self.name}')
        return True

with Test('first') as test:
    print(f'in {test.__class__.__name__}')

test = Test('second')
with test:
    print(f'in {test.__class__.__name__}')
