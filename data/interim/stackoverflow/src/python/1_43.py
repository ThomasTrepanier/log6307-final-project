def solution(sequence):
    
    if len(sequence) < 3: # since list with only 1 element is strictly increasing and 
                           # with 2 elements we can always remove 1 to make it strictly increasing
        return True 
    
    original_sequence = sequence.copy()
    # original_sequence = sequence
    # there is one problem with copying lists in this way. If you modify
#new_list, old_list is also modified. It is because the new list is
#referencing or pointing to the same old_list object.

    
    position_to_pop = 0 #this will be used to remember the position where the strictly increasing does not hold
    # for example 11,31,21,11 will give position_to_pop as index 2(21) in the for loop below...if it doesn't work then we remove the index 1 (31) to check whether it makes the list strictly increasing
    
    if is_sequence_increasing(sequence):
        return True
    else:
        for index, num in enumerate(sequence):
            if index != len(sequence) -1: # if statment since we want to loop until second last item
                if sequence[index+1] <= num:
                    position_to_pop = index + 1
                    break #breaking since we do not want to check further in the for loop
    
    sequence.pop(position_to_pop) #first removing right integer(index+1) where the problem occured
    
    if is_sequence_increasing(sequence):
        return True
    else: # if the first remove of the right integer doesn't work then we need to remove the left integer and see whether it fixes the issue 
        
        original_sequence.pop(position_to_pop-1)
        
        if is_sequence_increasing(original_sequence):
            return True
    
    return False

def is_sequence_increasing(sequence_to_check):
    
    for index, num in enumerate(sequence_to_check):
        if index != len(sequence_to_check) -1:
            if sequence_to_check[index+1] <= num:
                return False
    return True
