def sum_list(lis, n, X):
    """
    This function will return sum of all elemenst whose bit is set to 1 in X
    """
    sum_ = 0
    # print(X)
    for i in range(n):
        if (X & 1<<i ) !=0:
            # print( lis[i], end=" ")
            sum_ += lis[i]
    # print()
    return sum_

def return_list(lis, n, X):
    """
    This function will return list of all element whose bit is set to 1 in X
    """
    new_lis = []
    for i in range(n):
        if (X & 1<<i) != 0:
            new_lis.append(lis[i])
    return new_lis

lis = [5, 6, 2, 10, 2, 3, 4]
n = len(lis)
total = 2**n -1 

result_1 = 0
result_2 = total
result_1_sum = 0
result_2_sum = sum_list(lis,n, result_2)
ans = total
for i in range(total):
    x = (total ^ i)
    sum_x = sum_list(lis, n, x)
    sum_y = sum_list(lis, n, i)

    if abs(sum_x-sum_y) < ans:
        result_1 =  x
        result_2 = i
        result_1_sum = sum_x
        result_2_sum = sum_y
        ans = abs(result_1_sum-result_2_sum)

"""
Produce resultant list
"""

bucket_1 = return_list(lis,n,result_1)
bucket_2 = return_list(lis, n, result_2)

print("Bucket 1 : {}".format(bucket_1))
print("Bucket 2 : {}".format(bucket_2))


