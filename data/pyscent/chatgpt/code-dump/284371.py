# Defining the superclass
class Animal:
    def speak(self):
        return "Animal speaks!"

# Defining the subclass
class Dog(Animal): # Dog is a subclass of Animal
    # Overriding the speak method
    def speak(self):
        return "Woof!"

class Cat(Animal): # Cat is a subclass of Animal
    # Overriding the speak method
    def speak(self):
        return "Meow!"

# Creating objects
dog = Dog()
cat = Cat()

# Testing the overridden methods
print(dog.speak())  # Outputs: Woof!
print(cat.speak())  # Outputs: Meow!
