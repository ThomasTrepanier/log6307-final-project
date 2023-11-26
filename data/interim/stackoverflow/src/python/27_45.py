def state2(lst):
    if lst==[]:
        return True
    poped = lst.pop(0)
    if poped == "a":
        return state2(lst)
    else:
        if lst == [] or lst[0] == 'a':
            return False
        if lst[0]=="b":
            lst.pop(0) # removed "BB"
            return state1(lst)

def state1(lst):
    if lst==[]:
        return True
    if lst[0]=="a":
        lst.pop(0)
        return state2(lst)
    return False
