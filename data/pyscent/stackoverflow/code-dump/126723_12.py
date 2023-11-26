class MyClass:
    def action(self):
        print('first')

        self.next_action()

    def next_action(self):
        print('second')

my = MyClass()
my.action()
