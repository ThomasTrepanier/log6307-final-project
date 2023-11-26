def digital_root(n):
    # basic scenario: n is 1 digit, ergo <10. 
    if n < 10:
         return n

    # alternative case: more than 1 digit
    # cut n into digits with a list comprehension
    # str(714) => "714", list(str(714)) => "['7', '1', '4']
    digits = [int(c) for c in list(str(n))]

    # take the digital root of the sum
    return digital_root(sum(digits))
