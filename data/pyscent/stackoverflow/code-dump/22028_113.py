from enum import Enum

class RockPaperScissors(Enum):
    Rock = "rock"
    Paper = "paper"
    Scissors = "scissors"

    @property
    def beats(self):
        lookup = {
            RockPaperScissors.Rock: RockPaperScissors.Scissors,
            RockPaperScissors.Scissors: RockPaperScissors.Paper,
            RockPaperScissors.Paper: RockPaperScissors.Rock,
        }
        return lookup[self]
