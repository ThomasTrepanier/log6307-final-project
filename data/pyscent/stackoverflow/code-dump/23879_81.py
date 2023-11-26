class MyBitMask(BitMask):
    STR_TOKENS = string.ascii_uppercase
    def __init__(self, value=None, ignore=False):
        super().__init__(value, ignore)


print(str(MyBitMask(5)))
# AC
print(str(MyBitMask(15)))
# ABCD
