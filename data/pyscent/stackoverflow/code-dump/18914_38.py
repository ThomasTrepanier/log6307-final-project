class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return name

# Create a new instance with a name of your choice
some_person =  Person("XYZ")
# Call the greeting method
print(f"hi, my name is {some_person.name}")
