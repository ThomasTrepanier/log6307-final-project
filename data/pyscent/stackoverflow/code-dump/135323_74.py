from collections import Counter
def fitWord(placed,letters,maxLen=None):
    if maxLen is None:
        maxLen = len(placed)-placed.count(".")+len(letters)
    result = findwords(placed)
    if len(placed)<maxLen:
        result |= fitWord("."+placed,letters,maxLen)
        result |= fitWord(placed+".",letters,maxLen)
    letterCounts = Counter(letters)+Counter(placed.replace(".",""))
    return {w for w in result if not Counter(w)-letterCounts}
        
    
print(fitWord("l.p..n","eehatoi"))

# {'elaphine', 'elephant', 'lophine', 'lepton', 'oliphant'}
