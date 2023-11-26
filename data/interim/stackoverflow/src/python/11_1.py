def strip(group):
    non_overlapping=[]
    overlapping = [list(group.itertuples())[0]]
    end = list(group.itertuples())[0].to
    for row in list(group.itertuples())[1:]:
        if row[3]<=end:
            overlapping.append(row)
            if row.to > end:
                end = row.to
        else:
            non_overlapping.append(reduce_overlap(overlapping))
            overlapping=[row]
    non_overlapping.append(reduce_overlap(overlapping))
    return non_overlapping
