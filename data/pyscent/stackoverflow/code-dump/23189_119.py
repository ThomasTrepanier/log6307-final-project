class Char:
    def __init__(self, x, y):
        self.str = x
        self.con = y
        self.update()
    def update(self):
        self.hp = (self.con + self.str) / 2
