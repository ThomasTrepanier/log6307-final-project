class MyClass:
    @classmethod
    def action(cls, data):
        print('first')

        cls.next_action(data)

    @classmethod
    def next_action(cls, data):
        print('second', data)

MyClass.action('Hello World!')
