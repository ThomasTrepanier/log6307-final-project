def repeat(word, n, delim):
    str = ''
    for i in range(n): # this will repeat the next line n times.
        str += word + delim 
    return str[0:len(str) - len(delim)] # len(delim) will remove the last 'delim' from 'str'. 
