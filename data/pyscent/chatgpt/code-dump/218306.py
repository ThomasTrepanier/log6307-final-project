from abc import ABC, abstractmethod

class GameClient(ABC):
    
    @abstractmethod
    def chkForWin(self):
        pass

    @abstractmethod
    def chkDraw(self):
        pass

    @abstractmethod
    def isLegalMove(self, move):
        pass

    @abstractmethod
    def executeMove(self, move):
        pass

    @abstractmethod
    def printBoard(self):
        pass

    @abstractmethod
    def createGamePieces(self):
        pass

class Move(ABC):

    @abstractmethod
    def execute(self):
        pass

class GamePiece(ABC):
    
    @abstractmethod
    def getAvailableMoves(self):
        pass
