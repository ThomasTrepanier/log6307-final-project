d={'a':{1:1,2:2},"b":0,'c':"{}"}
print(d)
s=str(d)

dictionary_stack,dictionary_depth=0,0
def push():
    global dictionary_depth
    global dictionary_stack
    dictionary_stack+=1
    dictionary_depth=max(dictionary_depth,dictionary_stack)

def pop():
    global dictionary_stack
    dictionary_stack-=1

string_safety=False
for c in s:
    if c =="'":
        string_safety=not(string_safety)
    
    if not(string_safety) and c =='{':
        push()
    
    if not(string_safety) and c =='}':
        pop()


print(dictionary_depth)
