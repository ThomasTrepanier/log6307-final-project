numbers = [40, 40, 10, 10, 21, 21, 100,100, 400,400, 15, 15]
def second_lowest_number():
        numbers.sort()
        z = numbers[0]
for i in numbers:
        if i > z:
            print(i)
            break
second_lowest_number()
