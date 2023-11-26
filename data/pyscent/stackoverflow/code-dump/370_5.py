def fix_field_types(self):
    for key, value in self.asdict().items():
        field = self.__dataclass_fields__[key]
        if not field.type == type(value):
            new_value = field.type.__call__(value)
            self.__setattr__(field.name, new_value)
