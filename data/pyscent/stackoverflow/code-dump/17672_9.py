def reverse_string(string):
    length = len(string)
    
    mid = length//2
    # seperating in 3 parst
    first_half, second_half, middle = None, None, None
    
    # seperating string into first half, second half and mid based on length
    if length%2==1:
        first_half = string[:mid]
        second_half = string[mid+1:]
        middle = string[mid]
    else:
        first_half = string[:mid]
        second_half = string[mid:]
        
    # reversing the first half and second half
    first_half_reverse = first_half[::-1]
    second_half_reverse = second_half[::-1]
    
    # assembling the final result together
    final_result = None
    if middle is not None:
        final_result = first_half_reverse + middle + second_half_reverse
    else:
        final_result = first_half_reverse + second_half_reverse
    
    return final_result
