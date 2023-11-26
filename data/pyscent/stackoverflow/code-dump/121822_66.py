def sublength(string, char):
    try:
        start = string.index(char)
        end = string.index(char, start+1)
    except: return 'No two instances'
    else: return end +2
