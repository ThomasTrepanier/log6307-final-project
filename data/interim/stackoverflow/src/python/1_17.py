from django.db.models import Func, FloatField


class GeometryPointFunc(Func):
    template = "%(function)s(%(expressions)s::geometry)"

    def __init__(self, expression: Any) -> None:
        super().__init__(expression, output_field=FloatField())


class Latitude(GeometryPointFunc):
    function = "ST_Y"


class Longitude(GeometryPointFunc):
    function = "ST_X"
