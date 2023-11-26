def addNums(lst1, lst2, *args):
    numsIters = [iter(num[::-1]) for num in [lst1, lst2] + list(args)]  # make the iterators for each list
    carry, final = 0, []                                                # Initially carry is 0, 'final' will store the result
    
    while True:
        nums = [next(num, None) for num in numsIters]                   # for every num in numIters, get the next element if exists, else None
        if all(nxt is None for nxt in nums): break                      # If all numIters returned None, it means all numbers have exhausted, hence break from the loop
        nums = [(0 if num is None else num) for num in nums]            # Convert all 'None' to '0'
        digit = sum(nums) + carry                                       # Sum up all digits and carry
        final.append(digit % 10)                                        # Insert the 'ones' digit of result into final list
        carry = digit // 10                                             # get the 'tens' digit and update it to carry

    if carry: final.append(carry)                                       # If carry is non-zero, insert it
    return final[::-1]                                                  # return the fully generated final list

print(addNums([6, 9, 8], [5, 9, 2]))                                    # [1, 2, 9, 0]
print(addNums([7, 6, 9, 8, 8], [5, 9, 2], [3, 5, 1, 7, 4]))             # [1, 1, 2, 7, 5, 4]

