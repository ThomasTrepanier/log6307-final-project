import json
import enum
import datetime

class JsonDateEncoder(json.JSONEncoder):
    """JSON serializer for objects not serializable by default json code"""
    def default(self, o):
        if isinstance(o, (datetime.datetime, datetime.date)):
            return o.isoformat()
        return super().default(o)


class JsonEnumEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Enum):
            return o.name
        return super().default(o)

class Enumm(enum.Enum):
    X = enum.auto()

obj = {'time': datetime.datetime.now(), 'enum': Enumm.X}
encoder = MultipleJsonEncoders(JsonDateEncoder, JsonEnumEncoder)

In [502]: json.dumps(obj, cls=encoder)
Out[502]: '{"time": "2020-12-23T08:51:43.646022", "enum": "X"}'

