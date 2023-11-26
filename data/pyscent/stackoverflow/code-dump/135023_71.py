def isValidChessBoard(board: dict) -> bool:
    """Return True or False depending on if  a board is valid in chess."""
    board_pieces = list(board.values()) #initiate variable for repeated use
    all_pieces = ['king', 'queen', 'bishop','knight','rook','pawn']
    blacks, whites = 0, 0 #variable to keep count of black/white pieces
    
    def pCount(to_count: str) -> int:
        """Return count value of the piece"""
        return board_pieces.count(to_count)
        
    #check if board has one king and at most one queen for each side
    if (pCount('bking') != 1) or (pCount('wking') != 1) or \
       (pCount('bqueen') > 1) or (pCount('wqueen') > 1):
        return False  
    
    #check if all pieces names are valid 
    for piece in board_pieces:
        if piece[0] not in 'bw' or piece[1:] not in all_pieces:
            return False
                 
    #check if the position is valid (between 1a and 8h)
    for p in board.keys():
        if p[0] not in '12345678' or p[1] not in 'abcdefgh':
            return False
               
    #check if each side has a valid number of pieces
    for i in board_pieces:
        if i[0] == 'b':
            blacks += 1
        elif i[0] == 'w':
            whites += 1
    
    if (blacks or whites) > 16:
        return False
    elif (pCount('bpawn') or pCount('wpawn')) > 8:
        return False    
    elif (pCount('bbishop') or pCount('bknight') or pCount('brook')) > 2 \
    or   (pCount('wbishop') or pCount('wknight') or pCount('wrook')) > 2:
        return False
            
    return True
