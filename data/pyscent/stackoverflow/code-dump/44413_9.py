from datetime import timedelta

x = ['59:55:00', '59:55:00', '59:58:00', '1:00:02', '1:00:05', '1:01:26']

def converter(value, limit=59):
    var1, var2, var3 = map(int, value.split(':'))
    switch = var1 < limit
    mins = var1 * 60 + var2 if switch else var1
    secs = var3 if switch else var2
    return f'00:{mins:02}:{secs:02}'

res = list(map(converter, x))

print(res)
# ['00:59:55', '00:59:55', '00:59:58', '00:60:02', '00:60:05', '00:61:26']
