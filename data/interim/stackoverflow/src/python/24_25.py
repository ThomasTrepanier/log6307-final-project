class Test:
    my_string: str
    
    # You could use a dunder init method like this
    def __init__(self, target_string):
        """ This is the function that is ran upon Invoking the 
            class as an instance """
        self.my_string = target_string

    # Or you could not use the dunder init method and just have a class method like this. 
    # This way of doing so is not recommended though
    def set_string(self, target_string):
        """ Sets class instance variable 'mystring' to that of the 'target_string' parameter """
        self.my_string = target_string

# Then to set and retrieve the string from the class instance

# If using the __init__ method
tester_cls = Test('I am the target string')

print(tester_cls.my_string) # Prints 'I am the target string'

# or if using the set_string method
tester_cls = Test()
tester_cls.set_string('I am the target string')

print(tester_cls.my_string) # Prints 'I am the target string'

