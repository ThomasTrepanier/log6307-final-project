def findMedian(counter, d):
    count = 0
    median = 0

    if d%2 != 0:
        for i in range(len(counter)):
            count += counter[i]

            if count > d//2:
                median = i
                break
            
    else:
        first = 0
        second = 0

        for i, _ in enumerate(counter):
            count += counter[i]
            
            if first == 0 and count >= d//2:
                first = i
                
            if second == 0 and count >= d//2 + 1:
                second = i
                break
            
        median = (first+second) / 2
        
    return median


def activityNotifications(expenditure, d):
    count = 0
    counter = [0]*201
    
    for exp in range(d):
        counter[expenditure[exp]] += 1

    for i in range(d, len(expenditure)):
        new = expenditure[i]
        old = expenditure[i-d]
        median = findMedian(counter, d)
        
        if new >= 2*median:
            count += 1
            
        counter[old] -= 1
        counter[new] += 1
        
    return count
