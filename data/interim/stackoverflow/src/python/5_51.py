import operator

def get_overlaps(end, remaining):
    output = []
    for r in remaining:
        if r[0] < end:
            # starts before the end
            output.append(r[2])
            continue
        break
    return output

def get_all_overlaps(lst):
    # thanks @Elan-R for this simplification
    for i, (start, end, name) in enumerate(lst):        
        overlaps = get_overlaps(end, lst[i+1:])
        if overlaps:
            print(name, "overlaps", " & ".join(overlaps))


a = [(0, 98, '122:R'), (100, 210, '124:R'), (180, 398, '125:R'), (200, 298, '123:R')]

# sort by start time
a.sort(key=operator.itemgetter(0)) # thanks to @moonGoose
get_all_overlaps(a)
