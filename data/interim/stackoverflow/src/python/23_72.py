#!/usr/bin/env python3


# Using lists instead of sets for COLORS and PIECES should work.
#
#
# However, because it is important to stress that those constant define
# a *set* of permitted values, using sets sounds more acceptable.


# Please, note that sets are not explained in the chapter this exercise
# was taken from.

COLORS = {'b', 'w'}

PIECES = {
    'king',
    'queen',
    'rook',
    'bishop',
    'knight',
    'pawn'
    }

VALID_QUANTITY = {
    'king': (1, 1),
    'queen': (0, 1),
    'rook': (0, 2),
    'bishop': (0, 2),
    'knight': (0, 2),
    'pawn': (0, 8),
    }


# The following constants can be easily made using set('12345678') and
# set('abcdefgh').

ROWS = {'1', '2', '3', '4', '5', '6', '7', '8'}
COLUMNS = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}


# This function verifies if black pieces or white pieces quantity
# is correct, comparing the total pieces of each kind in the board, with
# the acceptable values defined in VALID_QUANTITY.

def verify_quantity(pieces):
    for piece, quantity in pieces.items():
        low, high = VALID_QUANTITY[piece]
        if low <= quantity <= high:
            return True
        else:
            return False


# This is the main function object of the exercise.

def is_valid_chess_board(board):
    
    black_pieces = {}
    white_pieces = {}
    
    for position, player_piece in board.items():
        
        row, column = position
        player = player_piece[0]
        piece = player_piece[1:]


        # First it is checked that the positions of the pieces, their
        # kind and colors are the ones allowed.
        
        if (row not in ROWS) or (column not in COLUMNS):
            return False
        if player not in COLORS:
            return False
        if piece not in PIECES:
            return False


        # The pieces present in the board are counted for each color.
        
        if player == 'b':
            black_pieces[piece] = black_pieces.get(piece, 0) + 1
        else:
            white_pieces[piece] = white_pieces.get(piece, 0) + 1


        # The quantity is finally checked to see if it is the one
        # allowed by the rules.
        
        if not(verify_quantity(black_pieces) or verify_quantity(white_pieces)):
            return False

    return True
