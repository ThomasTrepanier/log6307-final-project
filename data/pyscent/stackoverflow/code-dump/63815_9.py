def preProcesser(board: chess.Board):
    chess_dict = {
            1 : [1,0,0,0,0,0],
            2 : [0,1,0,0,0,0],
            3 : [0,0,1,0,0,0],
            4 : [0,0,0,1,0,0],
            5 : [0,0,0,0,1,0],
            6 : [0,0,0,0,0,1],
            0 : [0,0,0,0,0,0]
        }
    return torch.from_numpy(np.array([np.array(chess_dict[(board.piece_type_at(sq) if board.piece_type_at(sq) else 0)])*(-1 if board.color_at(sq)==False else 1) for sq in chess.SQUARES]).astype(np.float16).reshape(-1))
