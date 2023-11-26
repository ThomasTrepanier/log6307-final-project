with open("/usr/share/dict/words") as wf:
    words = [w.lower() for w in wf.read().split("\n") if len(w)>=2]

cIndex = dict()  # { (length,position,letter): set of words }
for word in words:
    for i,c in enumerate(word):
        cIndex.setdefault((len(word),i,c),set()).add(word)


def findwords(placed):
    result = None
    s = len(placed)
    for i,c in enumerate(placed):  #Run through known letters/positions
        if c=="." : continue
        if result is None:
            result  = cIndex.get((s,i,c),set()).copy()
        else:
            result &= cIndex.get((s,i,c),set())  # combine word sets
    return result or set()
