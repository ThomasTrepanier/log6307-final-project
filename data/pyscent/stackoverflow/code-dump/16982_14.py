blah = 'yada'

def foo(bar):
    global blah
    print(blah, bar)
    
foo('test') # output: yada test
