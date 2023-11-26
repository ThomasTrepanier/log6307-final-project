class Example:
    def print_x(self):
        print(self.x)

obj = Example()
obj.x = 5;    # Create a new attribute of the object and assign it a value 5
print(obj.x)  # Outputs 5
obj.print_x() # Outputs 5
