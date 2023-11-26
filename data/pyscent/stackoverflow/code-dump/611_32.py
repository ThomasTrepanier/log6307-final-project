from dataclasses import dataclass
from inspect import signature


def dataclass_init_kwargs(cls, *args, **kwargs):
    cls = dataclass(cls, *args, **kwargs)

    def from_kwargs(**kwargs):
        cls_fields = {field for field in signature(cls).parameters}
        native_arg_keys = cls_fields & set(kwargs.keys())
        native_args = {k: kwargs[k] for k in native_arg_keys}
        ret = cls(**native_args)
        return ret

    setattr(cls, 'from_kwargs', from_kwargs)
    return cls

