import typing
import types

def field_is_optional(cls: type, field_name: str):
    """A field is optional when it has Union type with a NoneType alternative.
    Note that Optional[] is a special form which is converted to a Union with a NoneType option
    """
    field_type = typing.get_type_hints(cls).get(field_name, None)
    origin = typing.get_origin(field_type)
    #print(field_name, ":", field_type, origin)
    if origin is typing.Union:
        return type(None) in typing.get_args(field_type)
    if origin is types.UnionType:
        return type(None) in typing.get_args(field_type)
    return False
