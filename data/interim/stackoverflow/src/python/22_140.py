import itertools
letters = {'2':'abc', '3':'def','4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs','8':'tuv', '9':'wxyz'}

def letterCombinations(digits):
    return ["".join(combo) for combo in itertools.product(*[letters[d] for d in digits])]

print(letterCombinations('23'))
