def isWinner(board, letter):
    return (
        (board[1] == board[2] ==  board[3] == letter) or
        (board[4] == board[5] ==  board[6] == letter) or
        (board[7] == board[8] ==  board[9] == letter) or
        (board[7] == board[4] ==  board[1] == letter) or
        (board[8] == board[5] ==  board[2] == letter) or
        (board[9] == board[6] ==  board[3] == letter) or
        (board[7] == board[5] ==  board[3] == letter) or
        (board[9] == board[5] ==  board[1] == letter))
