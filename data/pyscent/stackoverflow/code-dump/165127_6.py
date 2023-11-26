def inner_fib(acc, num):
    # acc is a list of two values 
    return [(acc[0]+acc[1]) % 997, (acc[0]+2*acc[1]) % 997]

def fib(n):
  return reduce(inner_fib, 
                range(2, n+1), # start from 2 since n=1 is covered in the base case
                [1,2])        # [1,2] is the base case

