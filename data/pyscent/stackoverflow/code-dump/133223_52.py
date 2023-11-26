def foo():
    global foo
    foo = 5
    print(foo + 5)

foo()  # OK, prints 10
