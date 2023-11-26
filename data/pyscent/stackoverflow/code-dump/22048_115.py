from enum import Enum

class RPS(Enum):
    Rock = 0
    Paper = 1
    Scissor = 2

    @property
    def beats(self):
        return list(RPS)[self.value - 1]

for v in RPS:
    print(v.name, 'beats', v.beats.name)
