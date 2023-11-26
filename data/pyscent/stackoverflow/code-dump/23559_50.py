NUM_ROWS = 3
NUM_COLS = 3
NUM_WIN = 3
BOARD_SIZE = NUM_ROWS * NUM_COLS

EMPTY = ' '
BOARD = [EMPTY] * BOARD_SIZE
TURNS = 'X', 'O'


def show_board(board):
    """Show the tic-tac-toe board."""
    for i in range(0, BOARD_SIZE, NUM_COLS):
        print(' | ' + ' | '.join(board[i:i + NUM_COLS]) + ' | ')


def ij(i, j):
    """Convert (row, col) to board index."""
    return i + NUM_COLS * j


def check_winner(board, turn):
    """Check if there is a winner."""
    # horizontal
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS - NUM_WIN + 1):
            if all(board[ij(i, j + k)] == turn for k in range(NUM_WIN)):
                return True
    # vertical
    for i in range(NUM_ROWS - NUM_WIN + 1):
        for j in range(NUM_COLS):
            if all(board[ij(i + k, j)] == turn for k in range(NUM_WIN)):
                return True
    # diagonal
    for i in range(NUM_ROWS - NUM_WIN + 1):
        for j in range(NUM_COLS - NUM_WIN + 1):
            K = NUM_WIN
            if all(board[ij(i + k, j + k)] == turn for k in range(NUM_WIN)):
                return True
            if all(board[ij(i + NUM_WIN - k - 1, j + k)] == turn
                   for k in range(NUM_WIN)):
                return True


def check_tie(board):
    """Check if tie."""
    return all(square != EMPTY for square in board)


def next_turn(turn):
    """Advance to next turn."""
    return TURNS[(TURNS.index(turn) + 1) % 2]


def main():
    """Tic-tac-toe game."""
    turn = TURNS[0]
    show_board(BOARD)
    while True:
        valid_input = False
        while not valid_input:
            try:
                choice = int(input(f'Player `{turn}` turn: '))
                valid_input = (1 <= choice <= BOARD_SIZE)
                if not valid_input:
                    raise ValueError
            except ValueError:
                print(f'Type numbers between 1 and {BOARD_SIZE} only.')
            else:
                idx = choice - 1
                if BOARD[idx] != EMPTY:
                    print(f'Position `{idx}` already taken by `{BOARD[idx]}`')
                else:
                    BOARD[idx] = turn

        show_board(BOARD)
        won = check_winner(BOARD, turn)
        if won:
            print(f'The winner is player `{turn}`!')
            break
        # handle a tie
        if not won and check_tie(BOARD):
            print('The match is a tie!')
            break
        turn = next_turn(turn)


if __name__ == '__main__':
    main()
