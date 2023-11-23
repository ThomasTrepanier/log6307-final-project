from abc import ABC, abstractmethod

class GameClient(ABC):

    @abstractmethod
    def createBoard(self, dimensions):
        pass

    @abstractmethod
    def printBoard(self, board):
        pass

class Game(ABC):
    def __init__(self, gameClient, dimensions):
        self.gameClient = gameClient
        self.board = self.gameClient.createBoard(dimensions)

    @abstractmethod
    def play(self):
        pass

class TicTacToeGame(Game):
    def play(self):
        # Implement the game play logic here

class TicTacToeGameClient(GameClient):
    def createBoard(self, dimensions):
        # Create a board with the given dimensions
        pass

    def printBoard(self, board):
        # Print the board 
        pass
