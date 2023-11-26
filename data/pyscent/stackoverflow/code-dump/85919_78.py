chars = 'abcdefghijklmnopqrstuvwxyz'
def repfree(s):
    for char in chars:
        count = s.count(char)
        if count > 1:
            return False
    return True
