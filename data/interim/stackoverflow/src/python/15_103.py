def car_refill(dist,cap,n,stops):
    stops.insert(0,0)
    stops.append(dist)
    num_refill,curr_refill = 0,0
    while curr_refill <= n:
        last_refill = curr_refill
        while (curr_refill <= n and stops[curr_refill + 1] - stops[last_refill] <= cap):
            curr_refill += 1
        if curr_refill == num_refill :
            return -1
        if curr_refill <= n:
            num_refill +=1
    return num_refill
