class Dog:
    SOUND = 'woof'
    def __init__(self, name):
        """Creates a new instance of the Dog class.

        This is the constructor in Python.
        The underscores are pronounced dunder so this function is called
        dunder init.
        """ 
        # this is an instance variable.
        # every time you instantiate an object (call the constructor)
        # you must provide a name for the dog
        self._name = name

    def name(self):
        """Gets the name of the dog."""
        return self._name

    @classmethod
    def bork(cls):
        """Makes the noise Dogs do.

        Look past the @classmethod as this is a more advanced feature of Python.
        Just know that this is how you would create a class method in Python.
        This is a little hairy.
        """
        print(cls.SOUND)
