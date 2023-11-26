users = list()

def check_continue():
    response = input('Continue? [y/n] ')

    if response == 'n':
        return False
    elif response == 'y':
        return True
    else:
        print('Please select a correct answer [y/n]')
        return check_continue()

while(True):
    std_name = input('Name: ')
    age_record = input('age: ')

    user = (std_name, age_record)
    users.append(user)

    if not check_continue():
        break
    else:
        continue

for name, age in users:
    print(name, '\t', user)
