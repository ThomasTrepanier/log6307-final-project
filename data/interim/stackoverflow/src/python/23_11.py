class MyClass:
    def action(self, data):
        print('first')

        self.next_action(data)

    def next_action(self, data):
        print('second', data)

instance = MyClass()
instance.action('Hello World!')
