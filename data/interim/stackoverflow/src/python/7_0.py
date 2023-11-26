def print_name():
    fname = input('Enter FIRST name here: ')
    if len(fname) == 0:
        raise Exception('No FIRST name entered...')

    lname= input('Enter LAST name here: ')
    if len(lname) == 0:
        raise Exception('No LAST name entered...')

    print(f"your name is {fname} {lname}")
