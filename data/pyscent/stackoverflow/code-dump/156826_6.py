class Test:

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f'entering {self.name}')
        return self

    def __exit__(self, exctype, excinst, exctb) -> bool:
        print(f'exiting {self.name}')
        return True

with Test('first') as test:
    print(f'in {test.name}')

test = Test('second')
with test:
    print(f'in {test.name}')
