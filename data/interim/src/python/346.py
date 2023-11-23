from abc import ABC, abstractmethod

class GameClient(ABC):

    @abstractmethod
    def createBoard(self, dimensions):
        pass

    @abstractmethod
    def printBoard(self, board):
        pass

    # Add any other methods here that would be common across all games.

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

    def checkForWin(self):
        # Check if a player has won the game

    def makeMove(self, move):
        # Make a move on the board

    # Add any other methods specific to Tic Tac Toe.

class TicTacToeGameClient(GameClient):
    def createBoard(self, dimensions):
        # Create a board with the given dimensions
        pass

    def printBoard(self, board):
        # Print the board 
        pass

    # Add any other methods specific to Tic Tac Toe.
