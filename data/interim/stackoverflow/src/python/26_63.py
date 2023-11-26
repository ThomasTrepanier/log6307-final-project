from collections import defaultdict
import inspect
import os


class PlatformFunction(object):
    mod_funcs = defaultdict(dict)

    @classmethod
    def get_function(cls, mod, func_name):
        return cls.mod_funcs[mod][func_name]

    @classmethod
    def set_function(cls, mod, func_name, func):
        cls.mod_funcs[mod][func_name] = func


def linux(func):
    frame_info = inspect.stack()[1]
    mod = inspect.getmodule(frame_info.frame)
    if os.environ['OS'] == 'linux':
        PlatformFunction.set_function(mod, func.__name__, func)

    def call(*args, **kwargs):
        return PlatformFunction.get_function(mod, func.__name__)(*args,
                                                                 **kwargs)

    return call


def windows(func):
    frame_info = inspect.stack()[1]
    mod = inspect.getmodule(frame_info.frame)
    if os.environ['OS'] == 'windows':
        PlatformFunction.set_function(mod, func.__name__, func)

    def call(*args, **kwargs):
        return PlatformFunction.get_function(mod, func.__name__)(*args,
                                                                 **kwargs)

    return call


@linux
def myfunc(a, b):
    print('linux', a, b)


@windows
def myfunc(a, b):
    print('windows', a, b)


if __name__ == '__main__':
    myfunc(1, 2)
