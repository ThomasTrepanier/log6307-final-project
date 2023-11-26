class Foo:
    def __init__(self):
        private = 'bar'
        def print_private():
            print(private)
        self.print_private = print_private

foo = Foo()
foo.print_private()  # works
foo.private  # kaboom
