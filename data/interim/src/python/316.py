def findTriplet(arr, target):
    arr.sort()  # Sort the array in ascending order
    n = len(arr)

    for i in range(n - 2):  # Loop through the array from the first element to the third-to-last element
        left = i + 1  # Initialize 'left' pointer to the next element after 'i'
        right = n - 1  # Initialize 'right' pointer to the last element of the array

        while left < right:  # Repeat until 'left' becomes greater than or equal to 'right'
            current_sum = arr[i] + arr[left] + arr[right]  # Calculate the sum of elements pointed by 'i', 'left', and 'right'
            if current_sum == target:  # If the sum equals the target, we found a triplet
                return True
            elif current_sum < target:  # If the sum is smaller, move the 'left' pointer to the right
                left += 1
            else:  # If the sum is greater, move the 'right' pointer to the left
                right -= 1

    return False  # If no triplet is found, return False
