def print_name():

    # store user input in separate variable
    first_name = input('Enter FIRST name here: ')

    fname = first_name



    while True:
        fname = first_name


        # throw error if user enters no first name
        if len(fname) == 0:
            # error msg
            print('No FIRST name entered...')
            first_name = input('Enter FIRST name here: ') 
            # loop back to prompt asking for first name
            continue
        else:
            # if first name given move on to prompting for last name
            # break loop
            break

    # loop into prompting user for last name
    while True:
        last_name = input('Enter LAST name here: ')
        lname= last_name

        # throw error if user enters no last name
        if len(lname) == 0:
            print('No LAST name entered...')
            # loop back to prompt asking for last name
            continue
        else:
            # if last name given move on to running print command
            # break loop
            break

        return fname, lname

    print(f'your name is {fname} {lname}')

print_name()
