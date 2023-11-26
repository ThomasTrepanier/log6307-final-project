x = 12     # this is an assignment, and because we're outside functions x
           # is deduced to be a global

def foo():
    print(x)     # we only "read" x, thus we're talking of the global

def bar():
    x = 3        # this is an assignment inside a function, so x is local
    print(x)     # will print 3, not touching the global

def baz():
    x += 3       # this will generate an error: we're writing so it's a
                 # local, but no value has been ever assigned to it so it
                 # has "no value" and we cannot "increment" it

def baz2():
    global x     # this is a declaration, even if we write in the code
                 # x refers to the global
    x += 3       # Now fine... will increment the global
