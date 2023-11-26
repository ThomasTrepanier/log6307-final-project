def min_refills(distance, tank, stops):
    stop_list = []
    stops.append(distance) # append the destination to the stop list
    # write your code here
    if distance <= tank: # if the travel distance <= distance travelled in one full tank
        return 0
    else:
        start = 0
        prev = 0
        for stop in stops:
            
            if stop - start < tank:     # if refueling stop is closer to the starting point than the car can travel in one full tank
                prev = stop     # move prev pointer to the refueling stop
            elif (stop - start == tank) and (stop != distance):     # don't consider destination as a refueling stop
                start = stop    # move the starting point to the current gas stop
                stop_list.append(stop)      # add the refueling stop to the stop list
                prev = stop     # move the prev pointer to the stop
            elif stop - start > tank:
                start = prev    # move the starting point to the prev gas stop
                if stop - start > tank:     # if next refuleing stop is farther than the dist. car can go in one full tank
                    return -1
                stop_list.append(prev)      # add the refueling stop to the list
                prev = stop     # move the prev pointer the stop

    return len(stop_list)
