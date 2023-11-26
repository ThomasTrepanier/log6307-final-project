def a(digits):
    """
    :type digits: str
    :rtype: List[str]
    """

    letters = {'2':'abc', '3':'def','4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs','8':'tuv', '9':'wxyz'}

    def backtrack(digits, path, res):
        if digits == '':
            res.append(path)
            return
        if len(digits) == 1:
            for letter in letters[digits[0]]:
                path += letter
                backtrack(digits[1:], path, res)
                path = path[:-1]
        else:
            for n in range(len(digits)-1):
                for letter in letters[digits[n]]:
                    path += letter
                    backtrack(digits[1:], path, res)
                    path = path[:-1]

    res = []
    backtrack(digits, '', res)
    return res
