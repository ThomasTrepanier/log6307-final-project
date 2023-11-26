import sys

class A:
    def __init__(self, x):
        self.x = x

    def __del__(self):
        print(f'A x={self.x} being destructed.')


a1 = A(1)
a2 = A(2)
a1 = None
# a1 is now destroyed
input('A(1) should have been destroyed by now ...')
a_list = [a2]
a_list.append(A(3))
a_list = None # A(3) should now be destroyed
input('A(3) should have been destroyed by now ...')
a4 = A(4)
sys.exit(0) # a2 and a4 may or may not be garbage collected
