def print_name():
    first_name = ""
    last_name = ""
    # User input for first name
    while first_name == "":
        first_name = input('Enter FIRST name here: ')
    # User input for last name
    while last_name == "":
        last_name = input('Enter LAST name here: ')
    print(f'your name is {first_name} {last_name}')
