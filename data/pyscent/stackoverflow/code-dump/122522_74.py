class Employee: 
  
    def __init__(self, name): 
        self.name = name
        print('Employee created.') 
    
    def get_name(self):
        return self.name

    def close(self):
        print("Object closed")

    # destructor
    def __del__(self):
        self.close()
  
obj = Employee('John')

print(obj.get_name())

# lets try deleting the object!
obj.__del__() # you don't need to run this

print("Program ends")

print(obj.get_name())
