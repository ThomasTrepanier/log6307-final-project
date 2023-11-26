class Account:
    last_code = 0
    def __init__(self) -> None:
        self.code = Account.last_code + 1
        Account.last_code = self.code

a = Account()
b = Account()
c = Account()

print(a.code) # 1
print(b.code) # 2
print(c.code) # 3
