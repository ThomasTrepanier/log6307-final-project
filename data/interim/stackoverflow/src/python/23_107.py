
board = {'1a': 'wrook', '1b': 'wknight', '1c': 'wbishop', '1d': 'wqueen', '1e': 'wking', '1f': 'wbishop',
'1g': 'wknight', '1h': 'wrook','2a': 'wpawn', '2b': 'wpawn', '2c': 'wpawn', '2d': 'wpawn', '2e': 'wpawn',
'2f': 'wpawn', '2g': 'wpawn', '2h': 'wpawn', '3a': '', '3b': '', '3c': '', '3d': '', '3e': '', '3f': '',
'3g': '', '3h': '', '4a': '', '4b': '', '4c': '', '4d': '', '4e': '', '4f': '', '4g': '', '4h': '',
'5a': '', '5b': '', '5c': '', '5d': '', '5e': '', '5f': '', '5g': '', '5h': '',
'6a': '', '6b': '', '6c': '', '6d': '', '6e': '', '6f': '', '6g': '', '6h': '',
'7a': 'bpawn', '7b': 'bpawn', '7c': 'bpawn', '7d': 'bpawn', '7e': 'bpawn', '7f': 'bpawn', '7g': 'bpawn', '7h': 'bpawn',
'8a': 'brook', '8b': 'bknight', '8c': 'bbishop' , '8d': 'bqueen', '8e': 'bking', '8f': 'bbishop',
'8g': 'bknight','8h': 'brook'}



def isValidChessBoard(board_dict):
    #check for 1 black king and 1 white king
    bking=0
    wking=0
    for king in board_dict.values():
        if king == 'bking':
            bking += 1
        if king == 'wking':
           wking += 1
    if bking != 1 or wking != 1:
        return False

    # check for 8 black pawns and 8 white pawns
    bpawn = 0
    wpawn = 0
    for pawn in board_dict.values():
        if pawn == 'bpawn':
            bpawn += 1
        if pawn == 'wpawn':
            wpawn += 1
    if wpawn != 8 or wpawn != 8:
        return False


    #check for valid spaces
    valid_spaces = {'1a', '1b', '1c', '1d', '1e', '1f', '1g', '1h','2a', '2b', '2c', '2d', '2e', '2f', '2g', '2h',
    '3a', '3b', '3c', '3d', '3e', '3f', '3g', '3h','4a', '4b', '4c', '4d', '4e', '4f', '4g', '4h',
    '5a', '5b', '5c', '5d', '5e', '5f', '5g', '5h','6a', '6b', '6c', '6d', '6e', '6f', '6g', '6h',
    '7a', '7b', '7c', '7d', '7e', '7f', '7g', '7h','8a', '8b', '8c', '8d', '8e', '8f', '8g', '8h'}

    spaces = set()
    for i in board_dict.keys():
        spaces.add(i) # use set add method (like append for lists)
    if spaces != valid_spaces:
        return False


    #check for 16 pieces per player
    piece_count = 0
    for piece in board_dict.values():
        if piece != '': # don't count the empty spaces (no pieces)
            piece_count += 1
    if piece_count != 32: # 16 x 2 = 32 total pieces
        return False

    return 'This is a valid board'


print(isValidChessBoard(board))
