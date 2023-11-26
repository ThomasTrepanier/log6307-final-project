class Math_Set_Base:
    @property
    def size(self):
        try:
            return self._size
        except:
            return len(self.elements)

    @size.setter
    def size(self, value):
        self._size = value
