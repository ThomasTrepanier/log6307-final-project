def repeatedString(s, n):
    count = 0
    for index, i in enumerate(s*n):
        if index >= n:
            return count
        if(i == 'a'):
            count += 1
    # empty string
    return count
