import functools
import inspect

@functools.cache
def get_dataclass_parameters(cls: type):
    return inspect.signature(cls).parameters


def instantiate_dataclass_from_dict(cls: type, dic: dict):
    parameters = get_dataclass_parameters(cls)
    dic = {k: v for k, v in dic.items() if k in parameters}
    return cls(**dic)
