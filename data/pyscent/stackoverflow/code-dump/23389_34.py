def find_two_sum(numbers, target_sum):
    for n in numbers:
        for i in numbers[numbers.index(n)+1:]:
            if n+i==target_sum:
                return(numbers.index(n),numbers.index(i))
                break
    return None

print(find_two_sum([3, 1, 5, 7, 5, 9], 10))
