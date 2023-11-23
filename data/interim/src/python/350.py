class TicTacToeBoard(Board):
    def __init__(self, boardDimensions):
        super().__init__(boardDimensions)
        self.createBoard()

    def createBoard(self):
        self.boardState = {i+1: ' ' for i in range(self.boardDimensions**2)}
