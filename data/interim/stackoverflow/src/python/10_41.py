def cellCompete(states,days):
    newstates = []
    added_states = [0] + states + [0]
    for counter,value in enumerate(states):
        newstates.append(int((added_states[counter] != added_states[counter+2])))

    if days > 1:
        return cellCompete(newstates,days-1)
    else:
        return newstates

print(cellCompete([1,1,1,0,1,1,1,1],2))
