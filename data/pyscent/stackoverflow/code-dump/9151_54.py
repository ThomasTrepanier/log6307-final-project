from enum import Enum
class MyEnum(Enum):
    state1=0
    state2=1

print (MyEnum.state1.name)  # 'state1'

a = MyEnum.state1
print(a.name)  # 'state1'
