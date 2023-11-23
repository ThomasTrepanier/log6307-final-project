class Game():
    Board board
    Algorithm algorithm
    List[Player] players

class Board():
    boardState
    boardDimensions

class Algorithm(ABC):
    @abstractmethod
    def calculateNextMove(self, board):
        pass

class Player(ABC):
    playerType
    playerLetter

    @abstractmethod
    def makeMove(self, board):
        pass

class HumanPlayer(Player):
    def makeMove(self, board):
        # Human makes a move

class ComputerPlayer(Player):
    def makeMove(self, board):
        # Computer makes a move

class MinimaxAlgorithm(Algorithm):
    def calculateNextMove(self, board):
        # Implement Minimax

class ReinforcementLearningAlgorithm(Algorithm):
    def calculateNextMove(self, board):
        # Implement RL
