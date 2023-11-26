from typing_extensions import Annotated
from datetime import datetime, timezone
from pydantic import BaseModel, PlainSerializer, BeforeValidator


CustomDatetime = Annotated[
    datetime,
    BeforeValidator(lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M%z').astimezone(tz=timezone.utc)),
    PlainSerializer(lambda x: x.strftime('%Y-%m-%dT%H:%M:%SZ'))
]


class MyModel(BaseModel):
    datetime_in_utc_with_z_suffix: CustomDatetime


if __name__ == "__main__":
    special_datetime = MyModel(datetime_in_utc_with_z_suffix="2042-3-15T12:45+01:00")  # note the different timezone

    # input conversion
    print(special_datetime.datetime_in_utc_with_z_suffix)  # 2042-03-15 11:45:00+00:00

    # output conversion
    print(special_datetime.model_dump_json())  # {"datetime_in_utc_with_z_suffix": "2042-03-15T11:45:00Z"}
