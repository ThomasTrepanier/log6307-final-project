def find_number(word): #returns the number present in the string
    for i in range(len(word)):
        if(word[i].isdigit()):
            num=""
            while(i<len(word) and word[i].isdigit()):
                num+=word[i]
                i+=1
            return int(num)
def order(sentence):
    od={}
    ct="a"
    for i in sentence.split():
        #numbering the strings so that if there are duplicates they are not lost
        od[ct+i]=find_number(i)
        ct=chr(ord(ct)+1)
    for i in sorted(od.values()):
        for j in od: #we can use other way of printing but this is the simplest but way less efficient
            if (od[j]==i):
                print(j[1:])
                break
s=input()
order(s)
