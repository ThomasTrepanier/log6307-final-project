class A:
    def __init__(self, a):
        self.a = a

class B(A):

    def printme(self):
        print(self.a)

b = B(10)
b.printme()
