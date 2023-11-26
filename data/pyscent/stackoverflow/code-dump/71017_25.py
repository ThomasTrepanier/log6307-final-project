# Define Wrapper Class
class Class():
    # Define __getitem__ method to be able to use index
    def __getitem__(self, type):
        # Define Main Class
        class Class():
            __doc__ = f"""I am an {type.__name__} class"""

            def __init__(self, value):
                self.value: type = type(value)
        # Return Class
        return Class
# Set Class to an instance of itself to be able to use the indexing
Class = Class()

print(Class[int].__doc__)
print(Class[int](5.3).value)
