import json

def dumps(object):
    def default(o):
        if isinstance(o, Enum):
            # use enum value when JSON deserialize the enum
            return o.__dict__['_value_'] 
        else:
            return o.__dict__
    return json.dumps(object, default=default)

print(json.dumps(YOUR_OBJECT_CONTAINS_ENUMS, default=default))
