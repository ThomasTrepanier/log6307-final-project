def makedate(s):
    return datetime.strptime( s, "%Y-%m-%d" )
def splitIntoRanges( dates ):
    ranges = []
    start_s = last_s = dates[0]
    last = makedate(start_s)
    for curr_s in dates[1:]:
        curr = makedate(curr_s)
        if (curr - last).days > 1:
            ranges.append((start_s,last_s))
            start_s = curr_s
        last_s = curr_s
        last = curr
    return ranges + [(start_s,last_s)]
