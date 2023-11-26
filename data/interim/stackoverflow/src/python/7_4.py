class Square_Integers_Below(Math_Set_Base):

    def __init__(self,cap):
        #Math_Set_Base.__init__(self)
        self.length = int(math.sqrt(cap))
        Math_Set_Base.size = self.length

    def __repr__(self):
        return str(self.size)
