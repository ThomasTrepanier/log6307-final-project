WIN_CASES = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
    [0, 4, 8], [2, 4, 6],  # diagonal
]


def check_winner(board, turn, win_cases=WIN_CASES):
    """Check if there is a winner."""
    for win_case in win_cases:
        if all(board[i] == turn for i in win_case):
            return True
