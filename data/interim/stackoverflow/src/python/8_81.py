from enum import IntEnum

class RPS(IntEnum):
    Rock = 1
    Paper = 2
    Scissor = 3

    def __lt__(self, other):
        if self == RPS.Scissor and other == RPS.Rock:
            return True
        if self == RPS.Rock and other == RPS.Scissor:
            return False
        return self.value < other.value

    def __gt__(self, other):
        if self == RPS.Rock and other == RPS.Scissor:
            return True
        if self == RPS.Scissor and other == RPS.Rock:
            return False
        return self.value > other.value
