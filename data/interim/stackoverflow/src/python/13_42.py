import shlex
from collections import OrderedDict

def f(text, **kwargs):
    split = shlex.split(text)
    d = OrderedDict(zip(split[::3], split[2::3]))
    d.update((k, d[k] + v) for k, v in kwargs.items() if k in d)
    return ' '.join('{} = "{}"'.format(k, v) for k, v in d.items())
