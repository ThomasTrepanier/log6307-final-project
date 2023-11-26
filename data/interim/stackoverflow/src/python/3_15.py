def pattern(size):
    for i in range(size):
        print('5'*i + '0' + '9'*(size-i-1))
        
pattern(4)
