L = ['house','cat','dog']
final = []
def substring(s):
    global final
    if len(s)==1:
        final.append(s)
    else:
        final.append(s)
        substring(s[:-1])
    return final

for s in L:
    substring(s)
print(final)
# ['house', 'hous', 'hou', 'ho', 'h', 'cat', 'ca', 'c', 'dog', 'do', 'd']
