class Square_Integers_Below(Math_Set_Base):

    def __init__(self, cap):
        self._size = int(math.sqrt(self._cap))

    @property
    def size(self):
        return self._size
