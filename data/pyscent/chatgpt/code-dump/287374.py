class CheesePizza:
    def prepare(self):
        return "Preparing Cheese Pizza"

class PepperoniPizza:
    def prepare(self):
        return "Preparing Pepperoni Pizza"

cheese_factory = CheesePizzaCreator()
result = cheese_factory.someOperation()  # This will internally create a CheesePizza object and call its prepare() method
print(result)  # Outputs: "Preparing Cheese Pizza"
