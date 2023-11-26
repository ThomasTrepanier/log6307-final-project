from enum import IntEnum

class RPS(IntEnum):
    Rock = 1 
    Paper = 2 
    Scissor = 3

RPS.Rock.beats = RPS.Scissor
RPS.Paper.beats = RPS.Rock
RPS.Scissor.beats = RPS.Paper

for i in [RPS.Rock,RPS.Paper,RPS.Scissor]:
    print(i, "beats", i.beats)
