class RPS(Enum):

    Rock = "rock"
    Paper = "paper"
    Scissors = "scissors"

    def __init__(self, value):
        if len(self.__class__):
            # make links
            all = list(self.__class__)
            first, previous = all[0], all[-1]
            first.beats = self
            self.beats = previous
