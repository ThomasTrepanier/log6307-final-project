class TestMeta(enum.EnumMeta):
    def __call__(cls, value, names=None, module=None, type=None, start=1):
        if names is not None:
            return enum.EnumMeta.__call__(cls, value, names, module, type, start)

        try:    
            return enum.EnumMeta.__call__(cls, value, names, module, type, start)
        except ValueError:
            return value
