def sol(word, board):
    rows = len(board)
    cols = len(board[0])
    coordinates = []
    wordCnt = 0
    co = []
    result = []
    def getWord(row, col, word, wordCnt, board):
        if row < 0 or col < 0 or row > len(board)-1 or col > len(board[0])-1 or wordCnt > len(word) -1 or board[row][col] != word[wordCnt]:
            return
        result.append(word[wordCnt])
        co.append((row, col))
        getWord(row+1, col, word, wordCnt+1, board)
        getWord(row, col+1, word, wordCnt+1, board)
        return co, result

    for row in range(rows):
        for col in range(cols):
            if board[row][col] == word[wordCnt]:
                co, result = getWord(row, col, word, wordCnt, board)
                if ''.join(result[-len(word):]) == word:
                    print(co[-len(word):])

                
sol('cat', board)
