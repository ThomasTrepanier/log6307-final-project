def main():

    from random import shuffle

    file_name = "text_database.txt"
    lines = open(file_name, "r").read().splitlines()
    shuffle(lines)

    sentinel = object()

    def command_random():
        try:
            line = lines.pop()
        except IndexError:
            print("There are no more lines in the file!")
        else:
            print(line)

    def command_quit():
        nonlocal sentinel
        sentinel = None

    commands = {
        "random": command_random,
        "quit": command_quit
    }

    while sentinel is not None:
        user_input = input("Please enter a command: ")
        command = commands.get(user_input)
        if command is None:
            continue
        command()

    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
