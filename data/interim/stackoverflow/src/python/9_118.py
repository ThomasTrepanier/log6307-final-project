class Char:

    def __init__(self, x, y):
        self.str = x
        self.con = y

    def get_hp(self):
        return (self.con + self.str) / 2

player = Char(20, 20)


def main(dude):
    print("strength:     " + str(dude.str))
    print("constitution: " + str(dude.con))
    print("hp: " + str(dude.get_hp()))
    print("------")
    action = input("press 1 to change str, 2 to change con")
    if action == "1":
        dude.str = dude.str + 10
        main(dude)
    elif action == "2":
        dude.con = dude.con + 10
        main(dude)
    else:
        main(dude)
