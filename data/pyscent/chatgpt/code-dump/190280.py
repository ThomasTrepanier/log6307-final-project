def countSubarraysWithSum(arr, target_sum):
    prefix_sum = 0
    sum_count = {0: 1}
    count = 0

    for num in arr:
        prefix_sum += num
        if prefix_sum - target_sum in sum_count:
            count += sum_count[prefix_sum - target_sum]
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1

    return count
