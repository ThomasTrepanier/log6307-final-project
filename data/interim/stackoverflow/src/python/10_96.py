name_array = list()
age_array = list()

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

    name_array.append(std_name)
    age_array.append(age_record)

    if not check_continue():
        break
    else:
        continue

for name, age in zip(name_array, age_array):
    print(name, '\t', age)
