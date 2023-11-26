def non_repetitive(list):

    list1=[]
    list2=[]

    for i in list:
        if not i in list1:
            list1.append(i)


    for j in list1:
        counter=0
        for k in list:
            if j==k:
                counter+=1
        list2.append(counter)


    return list1, list2



list=["jim","jennifer","roy","roy","mike","jim","roy","jim","mike","roy"]

print(non_repetitive(list))
