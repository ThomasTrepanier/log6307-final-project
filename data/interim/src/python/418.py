class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        super().speak()  # Calling the speak method from the Animal class
        print("Dog barks")

d = Dog()
d.speak()
