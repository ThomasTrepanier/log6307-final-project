def valid_chess_board(board):
    bpieces, wpieces = 0, 0
    pieces = ("king", "queen", "rook", "bishop", "knight", "pawn")
    board_pieces = list(board.values())

    # Checking the kings
    if board_pieces.count("bking") != 1 or board_pieces.count("wking") != 1:
        return False

    # Checking the pawns
    if board_pieces.count("bpawn") > 8 or board_pieces.count("wpawn") > 8:
        return False

    # Checking the colors
    for p in board_pieces:
        if p[0] == "b" and p[1:] in pieces:
            bpieces += 1
        elif p[0] == "w" and p[1:] in pieces:
            wpieces += 1
        else:
            return False

    # Checking the pieces
    if bpieces > 16 or wpieces > 16:
        return False

    # Checking the spaces
    for s in board:
        if s[0] not in "12345678" or s[1] not in "abcdefgh":
            return False

    return True

chess_board = {
    "1a": "wrook",
    "2a": "wpawn",
    "6a": "bpawn",
    "8a": "brook",
    "2b": "wpawn",
    "5b": "bpawn",
    "1c": "wbishop",
    "2c": "wbishop",
    "3c": "wpawn",
    "6c": "bknight",
    "7c": "bpawn",
    "1d": "wqueen",
    "2d": "wknight",
    "5d": "bpawn",
    "8d": "bqueen",
    "6e": "bbishop",
    "7e": "bbishop",
    "1f": "wrook",
    "2f": "wpawn",
    "3f": "wknight",
    "6f": "bknight",
    "8f": "brook",
    "1g": "wking",
    "2g": "wpawn",
    "7g": "bpawn",
    "8g": "bking",
    "2h": "wpawn",
    "7h": "bpawn",
}

print(valid_chess_board(chess_board))
