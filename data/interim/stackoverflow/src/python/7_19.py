class Math_Set_Base:
    _size = None

    def _size_call(self):
       return len(self.elements)

    @property
    def size(self):
        return  self._size if self._size is not None else self._size_call()

class Concrete_Math_Set(Math_Set_Base):
    def __init__(self, *elements):
        self.elements = elements


class Square_Integers_Below(Math_Set_Base):
    def __init__(self, cap):
        self._size = int(math.sqrt(cap))
