def positive_validator(name, value):
    if value <= 0:
        raise ValueError(f"values for {name!r}  have to be positive")

class MyAttr:
    def __init__(self, typ, validators=(), default=None):
        if not isinstance(typ, type):
            if isinstance(typ, tuple) and all([isinstance(t,type) for t in typ]):
                pass
            else:
                raise TypeError(f"'typ' must be a {type(type)!r} or {type(tuple())!r}` of {type(type)!r}")
        else:
            typ=(typ,)
        self.type = typ
        self.name = f"MyAttr_{self.type!r}"
        self.validators = validators
        self.default=default
        if self.default is not None or type(None) in typ:
            self.__validate__(self.default)
        
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, instance, owner):
        if not instance: return self
        return instance.__dict__[self.name]

    def __delete__(self, instance):
        del instance.__dict__[self.name]
        
    def __validate__(self, value):
        for validator in self.validators:
            validator(self.name, value)
            
    def __set__(self, instance, value):
        if value == self:
            value = self.default
        if not isinstance(value, self.type):
            raise TypeError(f"{self.name!r} values must be of type {self.type!r}")

        instance.__dict__[self.name] = value
        


#And now

@dataclass
class Person:
    name: str = MyAttr(str,[]) # required attribute, must be a str, cannot be none
    age: float = MyAttr((int, float), [positive_validator,],2) # optional attribute, must be an int >0, defaults to 2
    posessions: Union[list, type(None)] = MyAttr((list, type(None)),[]) # optional attribute in which None is default
