@dataclass
class MyClass:
   def setname(self, value):
       if not isinstance(value, str):
           raise TypeError(...)
       self.__dict__["name"] = value
   def getname(self):
       return self.__dict__.get("name")
   name: str = property(getname, setname)
   # optionally, you can delete the getter and setter from the class body:
   del setname, getname
