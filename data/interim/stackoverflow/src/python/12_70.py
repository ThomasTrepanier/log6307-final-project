def findWords(grid, words):
    # Regular old dfs through the grid, we only go right or down
    def dfs(row, col, path, idx):
        if idx == len(word):
            if word in all_paths:
                all_paths[word].append(list(path))
            else:
                all_paths[word] = [list(path)]
        else:
            if row + 1 < len(grid):
                if grid[row+1][col] == word[idx]:
                    path.append((row+1, col))
                    dfs(row+1, col, path, idx+1)
                    path.pop()
            if col + 1 < len(grid[0]):
                if grid[row][col+1] == word[idx]:
                    path.append((row, col+1))
                    dfs(row, col+1, path, idx+1)
                    path.pop()

    # For each word, find all possible paths through the grid to spell the word
    # Each path is a collection of coordinates as is desired from the function
    # Paths are indexed by word and stored in a list in a dictionary
    all_paths = {}
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            for word in words:
                if grid[row][col] == word[0]:
                    dfs(row, col, [(row, col)], 1)

    # Try all possible combinations of paths from each letter
    def dfs2(idx):
        if idx == len(words):
            return True

        word = words[idx]
        for path in all_paths[word]:
            for loc in path:
                if loc in seen:
                    return False
            for loc in path:
                seen.add(loc)
            if dfs2(idx+1):
                retlst.append(path)
                return True
            else:
                for loc in path:
                    seen.remove(loc)
        return False

    # Backtrack through possible combinations
    seen = set([])
    retlst = []
    dfs2(0)
    return retlst
