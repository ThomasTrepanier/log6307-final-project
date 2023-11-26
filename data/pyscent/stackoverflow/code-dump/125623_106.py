class FoobarEnum(Enum):
  FIRST = "foobar"
  SECOND = "baz"

  def __deepcopy__(self, memo):
      return self.value
