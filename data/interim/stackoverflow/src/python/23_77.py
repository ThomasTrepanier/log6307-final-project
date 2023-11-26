def isValidChessBoard(board):
    board = {'1a': 'brook', '1b': 'bknight', '1c': 'bbishop', '1d': 'bking', '1e': 'bqueen', '1f': 'bbishop',
             '1g': 'bknight', '1h': 'brook',
             '2a': 'bpawn', '2b': 'bpawn', '2c': 'bpawn', '2d': 'bpawn', '2e': 'bpawn', '2f': 'bpawn',
             '2g': 'bpawn', '2h': 'bpawn',
             '3a': '', '3b': '', '3c': '', '3d': '', '3e': '', '3f': '',
             '3g': '', '3h': '',
             '4a': '', '4b': '', '4c': '', '4d': '', '4e': '', '4f': '',
             '4g': '', '4h': '',
             '5a': '', '5b': '', '5c': '', '5d': '', '5e': '', '5f': '',
             '5g': '', '5h': '',
             '6a': '', '6b': '', '6c': '', '6d': '', '6e': '', '6f': '',
             '6g': '', '6h': '',
             '7a': 'wpawn', '7b': 'wpawn', '7c': 'wpawn', '7d': 'wpawn', '7e': 'wpawn', '7f': 'wpawn',
             '7g': 'wpawn', '7h': 'wpawn',
             '8a': 'wrook', '8b': 'wknight', '8c': 'wbishop', '8d': 'wking', '8e': 'wqueen', '8f': 'wbishop',
             '8g': 'wknight', '8h': 'wrook'
             }
    # Criteria 1 - 1 bbking and 1 wking

    count = {}

    for v in board.values():
        count.setdefault(v, 0)
        count[v] = count[v] + 1
    # print(count)
    # Criteria 2 - Each player can have at most 16 pieces, at most 8 pawns

    del count['']
    #print(count)
    pieces = 0
    for v in count.values():
        pieces = pieces + v
    #print(pieces)

    # Criteria 3 - All pieces must be on a valid space '1a' to '8h', not '9z'

    validSpace = {'1a': 'brook', '1b': 'bknight', '1c': 'bbishop', '1d': 'bking', '1e': 'bqueen', '1f': 'bbishop',
             '1g': 'bknight', '1h': 'brook',
             '2a': 'bpawn', '2b': 'bpawn', '2c': 'bpawn', '2d': 'bpawn', '2e': 'bpawn', '2f': 'bpawn',
             '2g': 'bpawn', '2h': 'bpawn',
             '3a': '', '3b': '', '3c': '', '3d': '', '3e': '', '3f': '',
             '3g': '', '3h': '',
             '4a': '', '4b': '', '4c': '', '4d': '', '4e': '', '4f': '',
             '4g': '', '4h': '',
             '5a': '', '5b': '', '5c': '', '5d': '', '5e': '', '5f': '',
             '5g': '', '5h': '',
             '6a': '', '6b': '', '6c': '', '6d': '', '6e': '', '6f': '',
             '6g': '', '6h': '',
             '7a': 'wpawn', '7b': 'wpawn', '7c': 'wpawn', '7d': 'wpawn', '7e': 'wpawn', '7f': 'wpawn',
             '7g': 'wpawn', '7h': 'wpawn',
             '8a': 'wrook', '8b': 'wknight', '8c': 'wbishop', '8d': 'wking', '8e': 'wqueen', '8f': 'wbishop',
             '8g': 'wknight', '8h': 'wrook'
             }

    if count['bking'] == 1:
        if count['wking'] == 1:
            if pieces == 32:
                if count['bpawn'] == 8:
                    if count['wpawn'] == 8:
                        if board == validSpace:
                            #return 'True: This is a Vaild Chessboard'
                            return True



chessBoardOne = {'1a': 'wrook', '1b': 'wknight', '1c': 'wbishop', '1d': 'wqueen', '1e': 'wking', '1f': 'wbishop',
'1g': 'wknight', '1h': 'wrook','2a': 'wpawn', '2b': 'wpawn', '2c': 'wpawn', '2d': 'wpawn', '2e': 'wpawn',
'2f': 'wpawn', '2g': 'wpawn', '2h': 'wpawn', '3a': '', '3b': '', '3c': '', '3d': '', '3e': '', '3f': '',
'3g': '', '3h': '', '4a': '', '4b': '', '4c': '', '4d': '', '4e': '', '4f': '', '4g': '', '4h': '',
'5a': '', '5b': '', '5c': '', '5d': '', '5e': '', '5f': '', '5g': '', '5h': '',
'6a': '', '6b': '', '6c': '', '6d': '', '6e': '', '6f': '', '6g': '', '6h': '',
'7a': 'bpawn', '7b': 'bpawn', '7c': 'bpawn', '7d': 'bpawn', '7e': 'bpawn', '7f': 'bpawn', '7g': 'bpawn', '7h': 'bpawn',
'8a': 'brook', '8b': 'bknight', '8c': 'bbishop' , '8d': 'bqueen', '8e': 'bking', '8f': 'bbishop',
'8g': 'bknight','8h': 'brook'}

print(isValidChessBoard(chessBoardOne))
#print(Answer)
