#Use str method instead of greeting() method
def __str__(self):
    # Should return "hi, my name is " followed by the name of the Person.
    return "hi, my name is {}".format(self.name) 
some_person = Person("xyz")  
# Call the __str__ method
print(some_person)
