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
        if isinstance(o, enum.Enum):
            return o.name
        return super().default(o)

class Enumm(enum.Enum):
    X = enum.auto()

obj = {'time': datetime.datetime.now(), 'enum': Enumm.X}
encoder = multiencoder_factory(JsonDateEncoder, JsonEnumEncoder)

json.dumps(obj, cls=encoder)
