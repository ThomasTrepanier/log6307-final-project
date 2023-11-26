class Square_Integers_Below(Math_Set_Base):
    size = None

    def __init__(self, cap):
        self.size = int(math.sqrt(cap))
