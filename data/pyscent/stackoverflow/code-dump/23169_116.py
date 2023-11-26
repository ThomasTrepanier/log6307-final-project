class Char:

    def __init__(self, x, y):
        self.str = x
        self.con = y

    @property
    def hp(self):
        # todo handle negative hp!
        return (self.con + self.str) / 2.


def test_hp():
    player = Char(20, 20)
    assert player.hp == 20


def test_hp_with_changes_to_con_or_str():
    player = Char(20, 20)
    player.con += 10
    assert player.hp == 25
    player.str += 10
    assert player.hp == 30
