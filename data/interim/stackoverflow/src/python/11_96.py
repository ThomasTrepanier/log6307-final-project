def seriesrun(x, n):
    power = 0
    s = 0

    while power < n:
        s += (-x)**power

        power +=1
    return s
