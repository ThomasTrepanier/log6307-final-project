def str_td(td):
    s = str(td).split(", ", 1)
    t = datetime.time(td.seconds // 3600,td.seconds // 60 % 60,td.seconds % 60, td.microseconds)
    s2 = s[:-1] + [str(t)]
    return ", ".join(s2)

print(str_td(datetime.timedelta(minutes=10)))
print(str_td(datetime.timedelta(minutes=3200)))
print(str_td(datetime.timedelta(minutes=-1400)))
print(str_td(datetime.timedelta(seconds=4003.2)))
print(str_td(datetime.timedelta(seconds=86401.1)))
