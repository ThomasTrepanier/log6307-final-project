def func(string):
    string +='@'
    dic = []
    tmp =[]
    tmp += [string[0]]

    for i in range(1,len(string)):

        if string[i]==string[i-1]:
            tmp.append(string[i])
        else:
            dic.append(tmp)
            tmp=[]
            tmp.append(string[i])
    res = ''.join(['{}{}'.format(len(i),i[0]) for i in dic])
    return res

string = 'ABBBBCCCCCCCCAB'         
solution = func(string)

print(solution)
