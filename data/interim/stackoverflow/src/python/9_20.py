class Char:
    def __init__(self, x, y):
        self.str = x
        self.con = y
        self.setHP()

    def __str__(self):
        text = "strength:     " + str(self.str) + "\n" +\
               "constitution: " + str(self.con) + "\n" +\
               "hp:           " + str(self.hp)
        return text

    def setHP(self):
        self.hp = (self.con + self.str) / 2

    def adjustStr(self, amount):
        self.str += amount
        self.setHP()

    def adjustCon(self, amount):
        self.con += amount
        self.setHP()


def main(dude):
    print(str(dude))
    print("------")
    action = input("press 1 to change str, 2 to change con")
    if action == "1":
        dude.adjustStr(10)
        main(dude)
    elif action == "2":
        dude.adjustCon(10)
        main(dude)
    else:
        main(dude)


player = Char(20, 20)

main(player)
