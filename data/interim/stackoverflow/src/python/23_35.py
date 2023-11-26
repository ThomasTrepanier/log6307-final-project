def foo():
    foo = "str"
    def inner():
#(1)    foo = 1 # Commented this line
        print(foo)
    inner()
    print(foo)

foo()
# str
# str

# Uncommenting (1) gives output as

foo()
# 1
# str
