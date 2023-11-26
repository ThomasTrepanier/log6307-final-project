class A:

    def __init__(self, field):

        self.methods = [self.method]
        self.field = field

    def __eq__(self, other):

        #Iterate through all keys
        for key in self.__dict__:
            #Perform comparison on values except the key methods
            if key != 'methods':
                if self.__dict__[key] != other.__dict__[key]:
                    return False

        return True

    def method(self):
        pass


first = A(field='foo')
second = A(field='bar')

print(first == second)
