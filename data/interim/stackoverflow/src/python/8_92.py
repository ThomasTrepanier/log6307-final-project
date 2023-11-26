def myfunc(string):
    # Un-hash print statements to watch python build out the string.
    # Script is an elementary example of using an enumerate function.
    # An enumerate function tracks an index integer and its associated value as it moves along the string.
    # In this example we use arithmetic to determine odd and even index counts, then modify the associated variable.
    # After modifying the upper/lower case of the character, it starts adding the string back together.
    # The end of the function then returns back with the new modified string.
    #print(string)
    retval = ''
    for space, letter in enumerate(string):
        if space %2==0:
            retval = retval + letter.upper()
            #print(retval)
        else:
            retval = retval + letter.lower()
            #print(retval)
    print(retval)
    return retval
myfunc('Thisisanamazingscript')
