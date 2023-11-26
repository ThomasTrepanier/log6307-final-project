#Issue is almost at the bottom
#Feel free to comment on the rest of the code as well,
#Always looking to improve
def main():
    loop = True
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
            return program1() # Return the output of this function
        elif answer == 2:
            return program2() # Return the output of this function
        elif answer == 3:
            return program3() # Return the output of this function
        else:
            loop = False

def program1():
    print('''This is program 1''')
    itdontwork = input('''Do you want to go back to the menu? Y/N''')

    if itdontwork == 'Y' or itdontwork == 'y':
        print()
    else:
        print('''SHUTTING DOWN''')
        return False # Return the output of this function

#The rest of the programs would be the same

main()
