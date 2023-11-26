#blah = 'yada'

def foo(bar):
    global blah
    print(blah, bar)
    
foo('test') # output: NameError: name 'blah' is not defined
