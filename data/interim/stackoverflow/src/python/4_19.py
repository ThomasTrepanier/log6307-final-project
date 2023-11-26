def summer_69(nums):
    total = 0
    ignore_section = False

    for num in nums:
        if num == 6:
            ignore_section = True
        elif num == 9:
            ignore_section = False
        elif not ignore_section:
            total += num

    return total
