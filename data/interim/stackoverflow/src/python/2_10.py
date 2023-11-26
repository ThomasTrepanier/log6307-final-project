def revStr(string):
    mid=len(string)//2
    if len(string)%2 != 0:
        x=string[:mid]
        middle=string[mid]
        y=string[mid+1:]
        print(x[::-1],middle,y[::-1],sep='')
    else:
        x=string[:mid]
        y=string[mid:]
        print(x[::-1],y[::-1],sep='')

revStr("abcdef")

