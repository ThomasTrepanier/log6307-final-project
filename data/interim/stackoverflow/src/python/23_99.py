board_width = ['1', '2', '3', '4', '5', '6', '7', '8']
board_height = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
board = []
for x in board_width:  #create a list of possible board positions
    for y in board_height:
        board.append(x + y)



pieces = ['king', 'queen', 'rook', 'rook',
          'bishop', 'bishop', 'knight', 'knight',
          'pawn', 'pawn', 'pawn', 'pawn', 'pawn',
          'pawn', 'pawn', 'pawn']    #list of all pieces for each player

white_pieces = pieces.copy()
black_pieces = pieces.copy()

def is_valid_chess_board(chess_dict):

    if 'wking' and 'bking' in chess_dict.values():

        for key, value in chess_dict.items(): #iterate each dict elements

            if value == '':
                board.remove(key)

            elif value.startswith('w') and key in board:  
                lis_val = list(value)
                lis_val.remove('w')
                val_str = "".join(lis_val)
                if val_str in white_pieces:
                    white_pieces.remove(val_str)
                    board.remove(key)
                    print(f"The White {val_str} was placed at {key}")
                else:
                    print(f"This {val_str} is not a proper Chess piece")

            elif value.startswith('b') and key in board:
                lis_val = list(value)
                lis_val.remove('b')
                val_str = "".join(lis_val)
                if val_str in black_pieces:
                    black_pieces.remove(val_str)
                    board.remove(key)
                    print(f"The Black {val_str} was placed at {key}")
                else:
                    print(f"This {val_str} is not a proper Chess piece")

            else:
                print("You have an incomplete Chess board")
                break
    else:
        print("You have an incomplete Chess board!")

    print(board)
