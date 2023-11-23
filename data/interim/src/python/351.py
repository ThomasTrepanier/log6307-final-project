class HumanPlayer(Player):
    def move(self, board):
        position = int(input("Enter your move: "))
        return position

class ComputerPlayer(Player):
    def __init__(self, letter, playerType, algorithm):
        super().__init__(letter, playerType)
        self.algorithm = algorithm

    def move(self, board):
        position = self.algorithm.move(board)
        return position
