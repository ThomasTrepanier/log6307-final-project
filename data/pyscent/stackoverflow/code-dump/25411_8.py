def mkd(*args):
    if len(args) == 1:
        print("Making", *args)
    else:
        print("mdk only takes 1 argument.")

def pwd(*args):
    if len(args) == 0:
        print("You're here!")
    else:
        print("pwd doesn't take any arguments.")

def add(*args):
    if len(args) == 2:
        if args[0].isdigit() and args[1].isdigit(): 
            print("Result:", int(args[0]) + int(args[1]))
        else:
            print("Can only add two numbers!")
    else:
        print("add takes exactly 2 arguments.")

def exit(*args):
    quit()


functions = {'mkd': mkd, 'pwd': pwd, 'add': add, 'exit': exit}  # The available functions.  

while True:
    command, *arguments = input("> ").strip().split(' ')  # Take the user's input and split on spaces.
    if command not in functions:
        print("Couldn't find command", command)
    else:
        functions[command](*arguments)
