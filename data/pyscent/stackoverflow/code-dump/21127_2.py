def wait_for_input(prompt):
    data = ""
    while data == "":
        data = input(prompt).strip()
    return data


def print_name(fname, lname):
    print(f'your name is {fname} {lname}')


first_name = wait_for_input('Enter FIRST name: ')
last_name = wait_for_input('Enter LAST name: ')

print_name(first_name, last_name)
