def findPair(arr, target):
    arr.sort()  # Sort the array in ascending order
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]  # Calculate the sum of elements pointed by 'left' and 'right'
        if current_sum == target:  # If the sum equals the target, we found a pair
            return True
        elif current_sum < target:  # If the sum is smaller, move the 'left' pointer to the right
            left += 1
        else:  # If the sum is greater, move the 'right' pointer to the left
            right -= 1

    return False  # If no pair is found, return False
