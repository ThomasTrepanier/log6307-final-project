class Car:
    # Class attribute to keep track of the total number of cars
    total_cars = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        # Increment the total_cars attribute when a new instance is created
        Car.total_cars += 1

    def __str__(self):
        return f"{self.make} {self.model}"

# Creating instances of the Car class
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")
car3 = Car("Ford", "Focus")

# Accessing the class attribute from an instance
print(f"Total number of cars: {car1.total_cars}")  # Output: 3
print(f"Total number of cars: {car2.total_cars}")  # Output: 3
print(f"Total number of cars: {car3.total_cars}")  # Output: 3
