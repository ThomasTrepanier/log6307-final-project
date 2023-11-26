def winner(votes):
    d = {}
    for i in votes:
        if i not in d:
            d[i]=1
        else:
            d[i] = d[i]+1

    # get the key for a value that's greater than half
    # or NOTA if there isn't one
    return next((k for k, v in d.items() if v > len(votes)//2), 'NOTA')

winner(['a','b','a','a','b','b', 'b'])
# 'b'

winner(['a','b','a','a','b','b'])
# NOTA
