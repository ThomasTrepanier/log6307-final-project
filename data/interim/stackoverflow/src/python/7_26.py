class Square_Integers_Below(Math_Set_Base):
    # explicitly define size at the class level to be literally anything other than a @property
    size = None

    def __init__(self,cap):
        self.size = int(math.sqrt(cap))

print(Square_Integers_Below(4).size)  # 2
print(Square_Integers_Below.size)     # None
