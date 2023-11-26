def sublist(a):
    i=0;
    lst=[];
    while(i<len(a) and a[i]!=5):
        lst.append(a[i]);
        i+=1;
    return lst;
