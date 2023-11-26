def nth_common(n,p):
    words=re.split('\W+',p.lower())
    word_count={}
    counter=0
    for i in words:
        if i in word_count:
            word_count[i]+=1
        else:
            word_count[i]=1

    sorted_count = sorted(word_count.items(), key=lambda x: x[1],reverse=True)         

    return sorted_count[n-1]
nth_common(3,paragraph)
