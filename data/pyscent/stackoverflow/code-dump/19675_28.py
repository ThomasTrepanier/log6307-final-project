def find_sum (n):
    sum_num = (n * (n + 1)) / 2
    return sum_num

n=int(input ("Enter a number: "))
result = str(find_sum(n))
print("The sum of first " + result)
