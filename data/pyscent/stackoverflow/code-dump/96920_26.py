s = set()
def get_input():
    return input('''Please type the number, when you're done please type "Done": ''')

for x in iter(get_input, "Done"):
    # x is guaranteed to *not* be Done here, or the loop
    # would have already exited.
    try:
        a = int(x)
    except ValueError:
        print("Integer only, please re-type")
        continue
    s.add(a)
