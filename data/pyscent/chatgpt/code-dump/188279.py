def subarraySum(arr, start, end):
    n = len(arr)
    prefix = [0] * n

    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]

    if start == 0:
        return prefix[end]
    else:
        return prefix[end] - prefix[start-1]
