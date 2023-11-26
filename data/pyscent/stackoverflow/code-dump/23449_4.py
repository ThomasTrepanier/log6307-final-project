import enum

class Fruits(enum.IntEnum):
    Apple = 0
    Cherry = 1
    Banana = 2

print(Fruits.Apple < Fruits.Banana) 
print(Fruits.Banana >= Fruits.Cherry) 
print(Fruits.Cherry < Fruits.Apple)
