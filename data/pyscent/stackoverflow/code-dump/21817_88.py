names = [["cat", 9112, "dog123", 5625],["luck", 1232, "bad23"]]
output = [no_duplicate(li) for li in names]

def no_duplicate(li):
    no_str = [no for no in li if type(no)==int] #get the numbers
    newlist = []
    for number in no_str:
        number = list(dict.fromkeys([s for s in str(number)])) #remove duplicate from each number
        number = "".join(x for x in number) 
        newlist.append(int(number)) #append back to the list they belong
    return newlist
