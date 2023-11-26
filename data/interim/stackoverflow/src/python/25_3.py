class Example:
    code = 0

    def __new__(cls, *args, **kwargs):
        cls.code += 1
        return super().__new__(Example, *args, **kwargs)


ex1 = Example()
print(ex1.code) # 1
ex2 = Example()
print(ex2.code) # 2
ex3 = Example()
print(ex3.code) # 3
