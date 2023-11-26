class Concrete_Math_Set(Math_Set_Base):
    def __init__(self,*elements):
        self.elements = elements

class Square_Integers_Below(Math_Set_Base):
    def __init__(self,cap):
        self.size = int(math.sqrt(cap))

print(Concrete_Math_Set(1,2,3).size) # 3
print(Square_Integers_Below(7).size) # 2
