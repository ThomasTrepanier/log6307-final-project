import string

def removeExceptFirst(s, old, new):
    i = s.find(old) + len(old)
    newStr = s[0:i]
    newStr += s[i:].replace(old, new)
    return newStr

print(removeExceptFirst("SELECT sdfdsf SELECT sdrrr SELECT 5445ff", "SELECT", "@@@SELECT"))
