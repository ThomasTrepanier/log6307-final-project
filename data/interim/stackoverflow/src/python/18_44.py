import json


class _DotDict(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


def dot(data=None):
    if data is []:
        return []
    return json.loads(json.dumps(data), object_hook=_DotDict) if data else _DotDict()
