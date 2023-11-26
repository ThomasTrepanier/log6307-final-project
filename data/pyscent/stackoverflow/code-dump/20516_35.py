def dec(s):
    s = s.rstrip('.')
    if(s.find('.') == -1): 
        return s
    else:
        i = s.find('.')
        return s[:i] + '.' + s[i+1:i+3]


print(dec('3.1415'))
print(dec('3'))
print(dec('1234.5678'))
print(dec('1234.5'))
print(dec('1234.'))
print(dec('1234'))
print(dec('.5678'))

3.14
3
1234.56
1234.5
1234
1234
.56
