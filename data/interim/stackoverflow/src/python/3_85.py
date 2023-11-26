def find_correct(word_dict):

    correct_count=0
    almost_correct_count=0
    wrong_count=0
    list1=[]
    for k,v in word_dict.items():
        if len(k)<=10:
            if len(k)==len(v):
                if k==v:
                    correct_count+=1
                else:
                    x=[]
                    y=[]
                    for i in k:
                        x.append(i)
                    for i in v:
                        y.append(i)
                    count=0
                    for i in x:
                        if not(y[x.index(i)]==i):
                            count+=1
                    if count<=2:
                        almost_correct_count+=1
                    else:
                        wrong_count+=1
            else:
                wrong_count+=1 
        else:
                wrong_count+=1          
    list1.append(correct_count)
    list1.append(almost_correct_count)  
    list1.append(wrong_count)      
    return list1       
word_dict={'MOST': 'MICE', 'GET': 'GOT', 'COME': 'COME', 'THREE': 'TRICE'}
print(find_correct(word_dict))
