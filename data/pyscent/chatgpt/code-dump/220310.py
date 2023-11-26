from abc import ABC, abstractmethod

class Board(ABC):
    def __init__(self, boardDimensions):
        self.boardDimensions = boardDimensions

    def getBoardDimensions(self):
        return self.boardDimensions

    def setBoardDimensions(self, boardDimensions):
        self.boardDimensions = boardDimensions
    
    @abstractmethod
    def getBoardState(self):
        pass

    @abstractmethod
    def setBoardState(self, boardState):
        pass

    @abstractmethod
    def createBoard(self):
        pass

    @abstractmethod
    def printBoard(self):
        pass

class TicTacToeBoard(Board):
    def __init__(self, boardDimensions):
        super().__init__(boardDimensions)

    def getBoardState(self):
        return self.boardState

    def setBoardState(self, boardState):
        self.boardState = boardState

    # create board. this will depend on the board dimensions
    def createBoard(self):
        boardDimensions = self.getBoardDimensions()
        boardState = {}
        for i in range(1, boardDimensions**2 + 1):
            boardState[i] = ' '
        self.setBoardState(boardState)
        self.printBoard()

    # print board. this will depend on the board dimensions
    def printBoard(self):
        boardState = self.getBoardState()
        boardDimensions = self.getBoardDimensions()
        if boardDimensions < 3 or boardDimensions > 10:
            print('Board dimensions not supported')
            return
        for i in range(1, boardDimensions**2 + 1):
            if i % boardDimensions == 0:
                print(boardState[i])
                if i != boardDimensions**2:
                    print('-'*(boardDimensions*2-1))
            else:
                print(boardState[i] + '|', end='')
        print('\n')
