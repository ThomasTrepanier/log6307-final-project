from typing import TypeVar, Type, Generic
T = TypeVar('T')

class Test(Generic[T]):

    def hello(self):
        print( "I am {0}".format(self.__orig_class__.__args__[0].__name__))

Test[int]().hello()
# I am int
