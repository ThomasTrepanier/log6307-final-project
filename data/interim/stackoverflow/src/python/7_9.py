class Math_Set_Base:
    @property
    def size(self):
        return len(self.elements)

    # size = property(lambda self: self.elements)


class Square_Integers_Below(Math_Set_Base):

    def __init__(self, cap):
        self._cap = cap

    @property
    def size(self):
        return int(math.sqrt(self._cap))

    # size = property(lambda self: int(math.sqrt(self._cap)))
