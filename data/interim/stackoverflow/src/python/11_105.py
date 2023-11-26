import collections

def nth_most(str_in, n):
    c = sorted(collections.Counter(w.lower() for w in str_in.split()).items(),key = lambda x:x[1])
    return(list(c[-n])) # convert to list as it seems to be the expected output

print(nth_most("apple apple apple blue BlUe call",2)) 
