# Program to Check whether given number is prime

def isPrime(number):
    limit = int(number/2) # limit indicates how many times we need to run the loop
    flag=0                # to keep track whether the number is prime or not
    if number==0 or number==1:
        print(f"The Given Number {number} is Not Prime")
        return
    for i in range(2,limit+1):
        if number%i==0:
            flag=1
            break
    if flag==0:
        print(f"The Given Number {number} is Prime")
    else:
        print(f"The Given Number {number} is Not Prime")
