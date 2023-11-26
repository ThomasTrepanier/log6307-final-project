@dataclass_json
@dataclass
class Command:
  param1: str
  param2: int


@dataclass_json
@dataclass
class Result:
  val1: str
  val2: int
