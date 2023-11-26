class A:
    def __init__(self, x):
        self.x = x
        self.cleanup_done = False
 
    def close(self):
        print(f'A x={self.x} being cleaned up.')
        self.cleanup_done = True
 
 
    def __del__(self):
        if not self.cleanup_done:
            self.close()
 
 
class B:
    def __init__(self, x):
        self.a = A(x)
 
    def foo(self):
        print("I am doing some work")
 
 
def bar():
    b = B(9)
    b.foo()
 
def other_function():
    pass
 
if __name__ == '__main__':
    bar()
    other_function()
