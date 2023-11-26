def repeatedString(s, n):
    # Get the length of input string
    strlen = len(s)
    a_repeat = 0
    # Get the total count of a repeated character from the input string
    for i in range(0,strlen):
        if s[i] == 'a':
            a_repeat = a_repeat + 1
    # Get the multiplier to make sure that desired input string length achieved
    str_multiplier = int(n // strlen) 
    # Get the repeated count if new string is been created
    result = a_repeat*str_multiplier
    new_str = s[:int( n % strlen )]
    # for odd length of string, get the remaining characters and find repated characters count and add up it to final count
    for i in range(0, len(new_str)):
        if new_str[i] == 'a':
            result += 1
    return result
