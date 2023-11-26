def find_correct(word_dict):
    correct,almost,incorrect=0,0,0
    for key,value in word_dict.items():
        count=0
        if(key==value):
            correct+=1
        elif(len(key)==len(value)):
            for i in range(0,len(key)):
                if(key[i]!=value[i]):
                    count+=1
            if(count<=2):
                almost+=1
            else:
                incorrect+=1
        else:
            incorrect+=1
    list=[correct,almost,incorrect]
    return list 

    word_dict={'WHIZZY': 'MIZZLY', 'PRETTY': 'PRESEN'}
    print(find_correct(word_dict))
