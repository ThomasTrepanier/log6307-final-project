#!/usr/bin/env python3.10

class MyClass:

    @classmethod
    def action(cls, data):
        print('first')

        MyClass.next_action(data)

    @classmethod
    def next_action(cls, data):
        print('second')

if __name__ == "__main__":
    myclass = MyClass()
    myclass.action('hmmm')
