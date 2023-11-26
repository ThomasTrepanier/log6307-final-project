def main():
    loop = True
    while loop:
        loop = program1()

def program1():
    itdontwork = input('''Do you want to go back to the menu? Y/N''')
    if itdontwork == 'Y' or itdontwork == 'y':
        print()
    else:
        print('''SHUTTING DOWN''')
        return False
