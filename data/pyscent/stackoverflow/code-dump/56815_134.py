def longest_weird(numbers):
    delta = list(set(range(max(numbers))).symmetric_difference(numbers))
    start,end = 0,0
    maxi = 0
    for i,x in enumerate(delta[:-1]):
        aux = max(maxi,delta[i+1]-x)
        if aux != maxi:
            start,end = (x+1,delta[i+1]-1)
            maxi = aux
    return numbers.index(start),numbers.index(end)
