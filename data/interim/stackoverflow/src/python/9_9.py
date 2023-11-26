import re

def make_replacer():
    rpl = ''
    def inner(m):
        nonlocal rpl
        res = rpl + m.group()
        rpl = '@@@'
        return res
    return inner

s = "SELECT sdfdsf SELECT sdrrr SELECT 5445ff"
res = re.sub(r'\bSELECT\b', make_replacer(), s)
print(res)   # SELECT sdfdsf @@@SELECT sdrrr @@@SELECT 5445ff
