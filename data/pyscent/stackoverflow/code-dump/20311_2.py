def reduce_overlap(overlapping):
    overlapping= sorted(overlapping,key=lambda x: x.value)
    if len(overlapping)==1 or overlapping[0].value != overlapping[1].value:
        return overlapping[0]
    else:
        return []
