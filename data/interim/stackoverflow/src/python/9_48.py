from operator import itemgetter
from itertools import chain 

winning_cases = {'diags' : [[0, 4, 8], [2, 4, 6]],
                 'rows': [[0, 1, 2], [3, 4, 5], [6, 7, 8]],
                 'cols': [[0, 3, 6], [1, 4, 7], [2, 5, 8]]}


def check_winner(board=board):
    for case in chain(*winning_cases.values()):
        candidates = set(itemgetter(*case)(board))
        if len(candidates) == 1 and '' not in candidates: # check if a diag, row or col has only one charcter
            winner, = candidates
            return winner


    return None 
