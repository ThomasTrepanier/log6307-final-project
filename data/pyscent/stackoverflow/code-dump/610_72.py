def __post_init__(self):
    for field in dataclasses.fields(self):
        value = getattr(self, field.name)
        if not isinstance(value, field.type):
            raise ValueError(f'Expected {field.name} to be {field.type}, '
                             f'got {repr(value)}')
            # or setattr(self, field.name, field.type(value))
