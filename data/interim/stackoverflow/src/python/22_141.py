def backtrack(digits, path, res):
    if len(digits) == 0:
        res.append(path)
    else:
        for letter in letters[digits[0]]:
            backtrack(digits[1:], letter + path, res)
