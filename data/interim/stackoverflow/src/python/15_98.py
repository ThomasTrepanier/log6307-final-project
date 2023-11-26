def para_check(checkme):
    open = ['(', '[', '{']
    close = [')', ']', '}']
    # assume that the result is true
    result = True

    # if the input is not a list then convert it to list
    if type(checkme) is not list:
        checkme = list(checkme)

    # if it doesnt contain at least 2 elements then return false
    if len(checkme) < 2:
        result = False

    # if number of closing and opening paranthesis is not the same then it is not balanced
    count_check1 = checkme.count('[') == checkme.count(']')
    count_check2 = checkme.count('(') == checkme.count(')')
    count_check3 = checkme.count('{') == checkme.count('}')

    # if not all of the above are true then it is unbalanced and thus...
    if not all([count_check1, count_check2, count_check3]):
        result = False

    def recurser(checkme, first, last):
        '''
        here start can be '[,(,{' and end can be '],),}' respectively,
        Check for a given type of bracket (any 1 of 3) see if the 
        index of the first closing bracket is greater than the first 
        opening bracket and if yes then remove them since they are a pair.
        Repeat this forever for all 3 types of brackets.
        '''            
        if first in checkme and last in checkme:
            open_index = checkme.index(first)
            closed_index = checkme.index(last)
            
            if closed_index > open_index:
                checkme.pop(closed_index)
                checkme.pop(open_index)
                # recursion
                recurser(checkme, first, last)
            else:
                result = False

    recurser(checkme, '[', ']')
    recurser(checkme, '(', ')')
    recurser(checkme, '{', '}')

    if len(checkme) > 0:
        result = False

    return result
