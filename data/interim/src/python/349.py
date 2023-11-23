class GameLogic():
    def __init__(self, board):
        self.board = board

    # other game logic methods...

    def insertLetter(self, letter, position):
        if (self.board.spaceIsFree(position)):
            self.board.setBoardState(position, letter)
            self.board.printBoard()
            if (self.chkDraw()):
                print('Draw!')
            elif winner := self.chkForWin():
                print(f'{winner} wins!')
            return
        else:
            print('Position taken, please pick a different position.')
            position = int(input('Enter new position: '))
            self.insertLetter(letter, position)
            return

class Board(ABC):
    # same as before...

class TicTacToeBoard(Board):
    # same as before...

# usage
board = TicTacToeBoard(3)
game = GameLogic(board)
