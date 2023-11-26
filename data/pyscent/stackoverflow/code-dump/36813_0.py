loop = True
def main():
    global loop
    while loop:
        print('''MENU CHOICE''')
        print('''1: go here''')
        print('''2: go there''')
        print('''3: You get the point''')
        print('''0: Terminate program''')
        print()

        try:
            answer = int(input('''I want to go to program: '''))
        except:
            print('''Not a valid menu choice, please try again''')
            print()

        if answer != 1 and answer != 2 and answer != 3 and answer != 0:
            print('''Not a valid menu choice, please try again''')
            print()
        elif answer == 1:
            program1()
        elif answer == 2:
            program2()
        elif answer == 3:
            program3()
        else:
            loop = False

def program1():
    global loop
    print('''This is program 1''')
    itdontwork = input('''Do you want to go back to the menu? Y/N''')

    if itdontwork == 'Y' or itdontwork == 'y':
        print()
    else:
        print('''SHUTTING DOWN''')
        loop = False #Here is the issue

#The rest of the programs would be the same

main()
