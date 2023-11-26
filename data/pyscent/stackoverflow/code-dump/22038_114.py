from enum import Enum

class RockPaperScissors(Enum):

    ROCK = ("rock", "scissors")
    PAPER = ("paper", "rock")
    SCISSORS = ("scissors", "paper")

    def __init__(self, value, beats):
        self._value_ = value
        self._beats = beats

    @property
    def beats(self):
        return getattr(RockPaperScissors, self._beats.upper())
