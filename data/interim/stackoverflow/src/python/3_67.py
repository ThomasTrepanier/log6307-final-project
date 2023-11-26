import sys
infi = sys.maxsize


def optimum_jump_recurse(arr, curr_pos, cost, path, res):
    if curr_pos in path or cost > res or curr_pos < 0:
        return infi
    elif curr_pos > len(arr) - 1:
        if cost < res:
            res = cost
        return cost

    res = optimum_jump_recurse(arr, curr_pos + 2, cost + arr[curr_pos],
                               path | {curr_pos}, res)
    backward_cost = optimum_jump_recurse(arr, curr_pos - 1,
                                         cost + arr[curr_pos],
                                        path | {curr_pos}, res)
    if res == backward_cost == infi:
        return res
    res = min(res, backward_cost)
    actual_cost = res - cost
    return res


nums = [1, 2, 3, 4, 100]
# nums = [1, 2, 3]
# nums = [1]
# nums = [1, 2]
# nums = [1, 2, 3, 100, 200]
# nums = [1, 1000, 3, 100, 200]
# nums = [1, 1, 3, 100, 200]
# nums = [1, 1, 3, 5, 100, 200]
# nums = [1, 2, 3, 100, 4]


def optimum_jump(nums):
    return optimum_jump_recurse(nums, 0, 0, set(), infi)


print(optimum_jump(nums))
