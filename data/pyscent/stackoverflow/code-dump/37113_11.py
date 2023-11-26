def convert(s):
    parts = [int(i) for i in s.split(":")]

    if parts[0] < 3:  # 3 is arbitrary value, may need adaption
        # Assuming format hour:min:sec
        h, m, s = parts
        millis = 0
    else:
        # Assuming format min:sec:millisec
        m, s, millis = parts
        h = 0

    return "1900-01-01 00:{:02}:{:02}".format(h * 60 + m, s)


x = ['59:55:00', '59:55:00', '59:58:00', '1:00:02', '1:00:05', '1:01:26']

print(*(convert(i) for i in x), sep="\n")
