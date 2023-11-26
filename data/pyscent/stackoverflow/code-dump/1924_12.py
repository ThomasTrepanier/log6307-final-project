def idataclass(**kwargs):     
    def deco(cls):
        cls = dataclass(cls, **kwargs)
        cls.__iter__  = lambda s: (getattr(s, field.name) for field  in fields(s))
        return cls
    return deco

 
@idataclass()
class XY:
    x: float | int
    y: float | int
