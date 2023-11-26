board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def show_board():# for showing the tic-tac-toe board
    print(' | ' + str(board[0]) + ' | ' +
          str(board[1]) + ' | ' + str(board[2]) + ' | ')
    print(' | ' + str(board[3]) + ' | ' +
          str(board[4]) + ' | ' + str(board[5]) + ' | ')
    print(' | ' + str(board[6]) + ' | ' +
          str(board[7]) + ' | ' + str(board[8]) + ' | ')


def main():
    one = 1
    flag = 1

    show_board()
    while one == 1:
        if flag == 1:
            x_o = 'X'
        if flag == 2:
            x_o = 'O'
        pos = int(input('Player "' + x_o + '" Turn: '))

        if x_o == 'o':
            x_o = 'O'
        if x_o == 'x':
            x_o = 'X'
        if board[pos - 1] == 'O' or board[pos - 1] == 'O':
            print('That Place Is Already Filled By Player "0"')

        if board[pos - 1] == 'X' or board[pos - 1] == 'X':
            print('That Place Is Already Filled By Player "X"')

        else:
            try:
                board[pos - 1] = x_o
            except IndexError:
                print('Type Numbers Between Only 1 And 9')

            if flag == 1:
                flag = 2
            elif flag == 2:
                flag = 1

            show_board()

            # Checking The Winner Of The Game
            won = False
            for turn in ('X', 'O'):
                # horizontal
                if not won:
                    for i in (0, 3, 6):
                        if all(board[i + k] == turn for k in range(3)):
                            won = True
                            break
                # vertical
                if not won:       
                    for i in range(3):
                        if all(board[i + k] == turn for k in (0, 3, 6)):
                            won = True
                            break
                # diagonal
                if not won:
                    if all(board[k] == turn for k in (0, 4, 8)) or \
                            all(board[k] == turn for k in (2, 4, 6)):
                        won = True
                # handle winning
                if won:
                    one = 2
                    print(f'The Winner Is Player "{turn}"!')
                    break
            # handle a tie
            if not won and all(square != ' ' for square in board):
                one = 2
                print('The Match Is A Tie!')


main()
