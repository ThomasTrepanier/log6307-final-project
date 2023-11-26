def findTriplet(arr, target):
    arr.sort()  # Sort the array in ascending order
    n = len(arr)

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == target:
                return True
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return False