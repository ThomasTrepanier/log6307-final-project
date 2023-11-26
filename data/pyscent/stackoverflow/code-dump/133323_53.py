def foo():
    global foo
    foo = 5
    print(foo + 5)

foo()  # OK, prints 10 (and incidentally assigns a new value to foo)
foo()  # Raises TypeError: 'int' object is not callable
