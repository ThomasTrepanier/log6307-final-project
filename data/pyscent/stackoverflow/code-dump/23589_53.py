o_list =['o', 'o', 'o']
x_list =['x', 'x', 'x']

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
    o_list =['o', 'o', 'o']
    x_list =['x', 'x', 'x']
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

            # for horizontal X
            if(board[0:3] == x_list or board[3:6] == x_list or board[6:9] == x_list or board[0:9:3] == x_list or board[1:9:3] == x_list or board[8:0:-3] == x_list):
                one = 2
                print('The Winner Is Player "X"!')

            if(board[0:3] == o_list or board[3:6] == o_list or board[6:9] == o_list or board[0:9:3] == o_list or board[1:9:3] == o_list or board[8:0:-3] == o_list):
                one = 2
                print('The Winner Is Player "O"!')

            elif board[0] != ' ' and board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and board[7] != ' ' and board[8] != ' ':
                print('The Match Is A Tie!')
                one = 2


main()
