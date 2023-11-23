from IPython.core.display import display, HTML
display(HTML("<style>.container { width:85% !important; }</style>"))

# Define the board
board={1:' ', 2:' ', 3:' ',
       4:' ', 5:' ', 6:' ',
       7:' ', 8:' ', 9:' '}

def printBoard(board):
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('\n')

printBoard(board)

def spaceIsFree(position):
    if (board[position]==' '):
        return True
    else:
        return False

def insertLetter(letter, position):
    if (spaceIsFree(position)):
        board[position]=letter
        printBoard(board)
        
        if (chkDraw()):
            print('Draw!')
        elif (chkForWin()):
            if (letter=='X'):
                print('Bot wins!')
            else:
                print('You win!')
        return
    else:
        print('Position taken, please pick a different position.')
        position=int(input('Enter new position: '))
        insertLetter(letter, position)
        return

def chkDraw():
    for key in board.keys():
        if (board[key]==' '):
            return False
    return True

def chkForWin():
    # (Include your conditions here)
    # ...

def chkMarkForWin(mark):
    # (Include your conditions here)
    # ...

player = 'O'
bot ='X'

def playerMove():
    position=int(input('Enter position for O:'))
    insertLetter(player, position)
    return

def compMove():
    bestScore=-1000
    bestMove=0
    for key in board.keys():
        if (board[key]==' '):
            board[key]=bot
            score = minimax(board, 0, False)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key
    insertLetter(bot, bestMove)
    return

def minimax(board, depth, isMaximizing):
    if (chkMarkForWin(bot)):
        return 1
    elif (chkMarkForWin(player)):
        return -1
    elif (chkDraw()):
        return 0
    if isMaximizing:
        bestScore = -1000
        for key in board.keys():
            if board[key]==' ':
                board[key]=bot
                score = minimax(board, 0, False)
                board[key]= ' '
                if (score>bestScore):
                    bestScore = score
        return bestScore
    else:
        bestScore = 1000
        for key in board.keys():
            if board[key]==' ':
                board[key]=player
                score = minimax(board, 0, True)
                board[key]= ' '
                if (score<bestScore):
                    bestScore = score
        return bestScore

while not chkForWin():
    compMove()
    playerMove()
