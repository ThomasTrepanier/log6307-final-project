from dataclasses import dataclass


@dataclass
class Container:
    user_id: int
    body: str

    def __new__(cls, *args, **kwargs):
        try:
            initializer = cls.__initializer
        except AttributeError:
            # Store the original init on the class in a different place
            cls.__initializer = initializer = cls.__init__
            # replace init with something harmless
            cls.__init__ = lambda *a, **k: None

        # code from adapted from Arne
        added_args = {}
        for name in list(kwargs.keys()):
            if name not in cls.__annotations__:
                added_args[name] = kwargs.pop(name)

        ret = object.__new__(cls)
        initializer(ret, **kwargs)
        # ... and add the new ones by hand
        for new_name, new_val in added_args.items():
            setattr(ret, new_name, new_val)

        return ret


if __name__ == "__main__":
    params = {'user_id': 1, 'body': 'foo', 'bar': 'baz', 'amount': 10}
    c = Container(**params)
    print(c.bar)  # prints: 'baz'
    print(c.body)  # prints: 'baz'`
