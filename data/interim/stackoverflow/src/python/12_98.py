from weakref import WeakKeyDictionary

class DependantAttribute:
    """Describes an attribute that is a fuction of other attributes.

    Only recalculates if one of the values it relies on changes. 
    'interns' the value and the values used to calculate it.
    This attribute must be set in the class's __init__

    name - the name of this instance attribute
    func - the function used to calculate the value
    attributes - instance attribute names that this attribute relies on
                 must match function parameter names
    mapping - not implemented: {attribute_name: function_parameter_name}

    """
    def __init__(self, name, func, attributes):
        self.name = name
        self.func = func
        self.attributes = attributes
        #self.mapping = None
        self.data = WeakKeyDictionary()

    def __get__(self, instance, owner):
        values = self.data.get(instance)
        if any(getattr(instance,attr) != values[attr]
               for attr in self.attributes):
            value = self.recalculate(instance)
            setattr(instance,self.name, value) 
        return self.data.get(instance)['value']

    def __set__(self, instance, value):
        # store the new value and current attribute values
        values = {attr:getattr(instance,attr) for attr in self.attributes}
        # validate?! : value == self.recalculate(**values)
        values['value'] = value
        self.data[instance] = values

    def recalculate(self, instance):
            # calculating a new value relies on
            # attribute_name == function_parameter_name
            kwargs = {attr:getattr(instance,attr) for attr in self.attributes}
            return self.func(**kwargs)
