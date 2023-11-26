def repeatedString(s, n):
    target = 'a'
    target_count = 0

    # how many times does the string need to be repeated: (n // len(s) * s) + s[:(n % len(s))] 
    quotient = n // len(s)
    remainder = n % len(s)

    for char in s:  # how many times target appears in 1 instance of the substring
        if char == target:
            target_count += 1
        
    # how many times the target appears in many instances of the substring provided
    target_count = target_count * quotient

    for char in s[:remainder]:  # count the remaining targets in the truncated substring
        if char == target:
            target_count += 1

    return target_count
