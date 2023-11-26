def isValid(board):
    # PUT TOGETHER A LIST OF ALL POSSIBLE PIECES
    pieces = ['king', 'queen', 'rook', 'knight', 'bishop', 'pawn']
    colors = ['b', 'w']
    all_pieces = {}
    possible_pieces = ['']
    color_count = {'b': 0, 'w': 0}
    for piece in pieces:
        for color in colors:
            possible_pieces.append('{}{}'.format(color, piece))
            all_pieces.setdefault('{}{}'.format(color, piece), 0)

    # CHECKS IF PIECES HAVE VALID NAMES
    for v in board.values():
        if v not in possible_pieces:
            print('Error: Invalid chess piece type')
            return False

    # ITERATE THROUGH BOARD, AND COUNT PIECES AND COLORS
    for k in board:
        if board.get(k) == '':
            continue
        all_pieces[board.get(k)] += 1      # INCREASE PIECE TYPE
        color_count[board.get(k)[0]] += 1  # INCREASE COLOR COUNT

    # CHECK TOTAL WHITE/BLACK PIECES
    if color_count['w'] > 16 or color_count['b'] > 16:
        print('Error: Invalid number of white or black pieces')
        return False

    # CHECKS IF VALID NUMBER OF PIECES
    for i in possible_pieces:
        num = all_pieces.get(i)
        if i == 'bking' or i == 'wking':
            if num != 1:
                print('Error: Invalid number of Kings')
                return False
        elif i == 'bqueen' or i == 'wqueen':
            if num > 1:
                print('Error: Invalid number of Queens')
                return False
        elif i == 'brook' or i == 'wrook':
            if num > 2:
                print('Error: Invalid number of Rooks')
                return False
        elif i == 'bknight' or i == 'wknight':
            if num > 2:
                print('Error: Invalid number of Knights')
                return False
        elif i == 'bbishop' or i == 'wbishop':
            if num > 2:
                print('Error: Invalid number of Bishops')
                return False
        elif i == 'bpawn' or i == 'wpawn':
            if num > 8:
                print('Error: Invalid number of Pawns')
                return False

    # CHECK ALL VALID SPACES
    for s in board:
        if s[0] not in '12345678' or s[1] not in 'abcdefgh':
            print('Error: Space is not valid!')
            return False

    # IF PASS ALL CHECKS, THE BOARD IS VALID 
    return True
