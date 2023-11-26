def str_td(td):
    s = str(td).split(", ", 1)
    a = s[-1]
    if a[1] == ':':
        a = "0" + a
    s2 = s[:-1] + [a]
    return ", ".join(s2)

print(str_td(datetime.timedelta(minutes=10)))
print(str_td(datetime.timedelta(minutes=3200)))
print(str_td(datetime.timedelta(minutes=-1400)))
print(str_td(datetime.timedelta(seconds=4003.2)))
print(str_td(datetime.timedelta(seconds=86401.1)))
