import re

def remove_duplicates_helper(s):
    words = (x.group(0) for x in re.finditer(r"[^\s]+", s))
    current = None
    for word in words:
        if word != current:
            yield word
            current = word

def remove_duplicates(s):
    return ' '.join(remove_duplicates_helper(s))

mystring = "my friend's new new new new and old old cats are running running in the street"
print(remove_duplicates(mystring))
