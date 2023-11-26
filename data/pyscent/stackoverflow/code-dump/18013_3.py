def whatistheremainder(v):
    remainderforone = v.split(' ', 1)
    outcome = remainderforone[1:][0]
    return outcome
print(whatistheremainder('the quick brown fox'))
