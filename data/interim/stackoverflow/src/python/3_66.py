from json import JSONEncoder
from typing import Any, Type

class CombinedEncoder():
    """
    Combine multiple JSON encoders
    https://stackoverflow.com/questions/65338261/combine-multiple-json-encoders
    """
    def __new__(cls, *encoders: Type[JSONEncoder]):
        def default(o: Any, *args: bool, **kwargs: bool) -> str | Any:
            for encoder in encoders:
                try:
                    return encoder(*args, **kwargs).default(o)
                except TypeError:
                    pass
            raise TypeError(
                f'Object of type {o.__class__.__name__} is not JSON serializable')

        encoder = type(
            "CombinedEncoder",
            (JSONEncoder,),
            {
                "default": default,
                "__doc__": "Combines JSONEncoders"
            }
        )
        return encoder
