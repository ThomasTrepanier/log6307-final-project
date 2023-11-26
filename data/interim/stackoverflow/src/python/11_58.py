def solve(arr):
    res = []
    req = 4-len(arr)

    while req>0:
      for i in range(len(arr)):
        res.append(arr[i])
        req = req-1
        if req == 0:
          break

    return arr+res

num = [4, 2]
res_num = solve(num)
print(res_num)

num = [9, 3, 12]
res_num = solve(num)
print(res_num)

num = [3]
res_num = solve(num)
print(res_num)
