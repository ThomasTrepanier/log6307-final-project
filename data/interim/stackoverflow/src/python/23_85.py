import sys

res = []
def hailstone(number):
    global res
    
    if number > 1:
        if number % 2 == 0:
            res.append( number // 2 )
            hailstone(res[len(res)-1])
        else:
            res.append(number * 3 + 1) 
            hailstone(res[len(res)-1])

    return res




number = int(input('Enter a positive integer. To quit, enter -1: '))
if number <= 0 or number == 0:
    print('Thank you for playing Hailstone.')
    sys.exit()

else:
    answers = hailstone(number)
    for answer in answers:
        print(answer)
    print('The loop executed {} times.'.format(len(answers) + 1))
