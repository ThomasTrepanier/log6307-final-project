class MyClass:

    @classmethod
    def my_method(cls):
        return "class method"

    @staticmethod
    def my_other_method():
        return "static method"

    def yet_another_method(self):
        return yet_another_method()

# Class definition ends here. You can now define another function that
# can be imported like you want to do it, and, if needed, used to define
# a class method of the same name.

def yet_another_method():
    return "works too"
