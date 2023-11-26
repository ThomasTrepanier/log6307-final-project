def compute_min_number_of_refills(d, m, stops):
    if d <= m:
        return 0
    total_refill = 0
    last_refill = -1
    limit = m 
    stops.append(d)
    i = 0
    while i < len(stops):
        if stops[i] >= limit: 
            current_refill = i - 1 if stops[i] > limit else i
            if current_refill == last_refill:
                return -1 
            last_refill = current_refill
            total_refill += 1
            limit = m + stops[current_refill]
            i = current_refill + 1
        else:
            i += 1
    return total_refill
