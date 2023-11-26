from bisect import bisect_left

def find_words(board, words, x, y, prefix, path):
    ' Find words that can be generated starting at position x, y '
    
    # Base case
    # find if current word prefix is in list of words
    found = bisect_left(words, prefix)  # can use binary search since words are sorted
    if found >= len(words):
        return
   
    if words[found] == prefix:
        yield prefix, path              # Prefix in list of words

    # Give up on path if what we found is not even a prefix
    # (there is no point in going further)
    if len(words[found]) < len(prefix) or words[found][:len(prefix)] != prefix:
        return
    
    # Extend path by one lettter in boarde
    # Since can only go right and down 
    # No need to worry about same cell occurring multiple times in a given path
    for adj_x, adj_y in [(0, 1), (1, 0)]:
        x_new, y_new = x + adj_x, y + adj_y
        if x_new < len(board) and y_new < len(board[0]):
            yield from find_words(board, words, x_new, y_new, \
                                  prefix + board[x_new][y_new], \
                                  path + [(x_new, y_new)])
     
def check_all_starts(board, words):
    ' find all possilble paths through board for generating words '
    # check each starting point in board
    for x in range(len(board)):
        for y in range(len(board[0])):
            yield from find_words(board, words, x, y, board[x][y], [(x, y)])
   
def find_non_overlapping(choices, path):
    ' Find set of choices with non-overlapping paths '
    if not choices:
        # Base case
        yield path
    else:
        word, options = choices[0]

        for option in options:
            set_option = set(option)
            
            if any(set_option.intersection(p) for w, p in path):
                # overlaps with path
                continue
            else:
                yield from find_non_overlapping(choices[1:], path + [(word, option)])
        
    
def solve(board, words):
    ' Solve for path through board to create words '
    words.sort()
    
    # Get choice of paths for each word
    choices = {}
    for word, path in check_all_starts(board, words):
        choices.setdefault(word, []).append(path)
    
    # Find non-intersecting paths (i.e. no two words should have a x, y in common)
    if len(choices) == len(words):
        return next(find_non_overlapping(list(choices.items()), []), None)
    
