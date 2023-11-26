piece = {}


# enter chess piece and position
def pieceSet():
    while True:
        print("Enter chess piece: (start with 'b' or 'w' + piece) or  enter 'q' to exit")
        pc = str(input())
        if pc == 'q':
            break
        print("Place the piece on the chess board: ")
        position = str(input())
        piece[str(position)] = str(pc)


def isValidChessBoard():
    # board position and coordinates
    board = []
    for row in range(1, 9):
        for col in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'):
            board.append(str(row)+str(col))

    # check if both kings are still on the board
    if 'wking' not in piece.values() or 'bking' not in piece.values():
        print('---The Board is Invalid!---')
        print("King is not on the board!")
        return False

    # check the position of every piece on the board
    for key in piece.keys():
        if key not in board:
            print('---The Board is Invalid!---')
            print("Chess Board only has 8 boxes per row ('a' to 'h') and 8 boxes percolumn ('1 to 8')")
            return False

    # check if the name starts with a "w" or "b"
    for pieces in piece.values():
        if pieces[0] != "b" and pieces[0] != "w":
            print('---The Board is Invalid!---')
            print("Chess pieces only have 2 colors: (b)lack and (w)hite")
            return False

    # check the quantity of every chess pieces and see if every piece is valid
    bpawn = 0
    wpawn = 0
    bking = 0
    wking = 0
    bqueen = 0
    wqueen = 0
    bbishop = 0
    wbishop = 0
    bknight = 0
    wknight = 0
    brook = 0
    wrook = 0
    for value in piece.values():
        if value == 'bpawn':
            bpawn += 1
            if bpawn > 8:
                print('---The Board is Invalid!---')
                print("Exceeded the limit of bpawn!")
                return False
            else:
                continue
        elif value == 'wpawn':
            wpawn += 1
            if wpawn > 8:
                print('---The Board is Invalid!---')
                print("Exceeded the limit of wpawn!")
                return False
            else:
                continue
        elif value == 'bking':
            bking += 1
            if bking > 1:
                print('---The Board is Invalid!---')
                print("Exceeded the limit of bking!")
                return False
            else:
                continue
        elif value == 'wking':
            wking += 1
            if wking > 1:
                print('---The Board is Invalid!---')
                print("Exceeded the limit of wking!")
                return False
            else:
                continue
        elif value == 'bqueen':
            bqueen += 1
            if bqueen > 1:
                print('---The Board is Invalid!---')
                print("Exceeded the limit of bqueen!")
                return False
            else:
                continue
        elif value == 'wqueen':
            wqueen += 1
            if wqueen > 1:
                print('---The Board is Invalid!---')
                print("Exceeded the limit of wqueen!")
                return False
            else:
                continue
        elif value == 'bbishop':
            bbishop += 1
            if bbishop > 2:
                print('---The Board is Invalid!---')
                print("Exceeded the limit of bbishop!")
                return False
            else:
                continue
        elif value == 'wbishop':
            wbishop += 1
            if wbishop > 2:
                print('---The Board is Invalid!---')
                print("Exceeded the limit of wbishop!")
                return False
            else:
                continue
        elif value == 'bknight':
            bknight += 1
            if bknight > 2:
                print('---The Board is Invalid!---')
                print("Exceeded the limit of bknight!")
                return False
            else:
                continue
        elif value == 'wknight':
            wknight += 1
            if wknight > 2:
                print('---The Board is Invalid!---')
                print("Exceeded the limit of wknight!")
                return False
            else:
                continue
        elif value == 'brook':
            brook += 1
            if brook > 2:
                print('---The Board is Invalid!---')
                print("Exceeded the limit of brook!")
                return False
            else:
                continue
        elif value == 'wrook':
            wrook += 1
            if wrook > 2:
                print('---The Board is Invalid!---')
                print("Exceeded the limit of wrook!")
                return False
            else:
                continue
        else:
            print('---The Board is Invalid!---')
            print(str(value) + " piece not included!")
            return False


def result():
    if isValidChessBoard() == False:
        return False
    else:
        print('---The Board is Valid!---')
        return True


pieceSet()
print('piece =', piece)
print(result())
