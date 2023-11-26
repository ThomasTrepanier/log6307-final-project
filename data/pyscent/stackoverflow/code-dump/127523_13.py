#!/usr/bin/env python3.10

class MyClass:
    def action(self, data):
        print('first')

        self.next_action(data)

    def next_action(self, data):
        print('second')

if __name__ == "__main__":
    myclass = MyClass()
    myclass.action('hmmm')
