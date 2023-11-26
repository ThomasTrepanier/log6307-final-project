from sys import exit


def check_number(number):
    
    if number % 2 ==0:
        print(number // 2)
        return(number // 2)
    else:
        print(number*3+1)
        return number*3+1

def user_call(number):
    count = 0
    while number != 1:
        count += 1
        number = check_number(number)
    return count


if __name__ == "__main__":
    
    try:
        number = int(input('Give a number \n'))
        count = user_call(number)
        print('count ',count)

    except Exception as e:
        exit()
