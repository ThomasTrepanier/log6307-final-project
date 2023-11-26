def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """

    letters = {'2':'abc', '3':'def','4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs','8':'tuv', '9':'wxyz'}

    def backtrack(digits, path, res):
        if digits == '':
            res.append(path)
            return
        for letter in letters[digits[0]]:

            # note that you can replace this section with 
            # backtrack(digits[1:], path + letter, res)

            path += letter
            backtrack(digits[1:], path, res)
            path = path[:-1]


    res = []
    backtrack(digits, '', res)
    return res

letterCombinations('23')
