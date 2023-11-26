def balanced(s):
    if s.count('[') == s.count(']') and s.count('(') == s.count(')') and s.count('{') == s.count('}'):
        return True
    else:   
        return False
