#!/usr/bin/env python

import sys
import time
import math

def next_prime(number):
    if number < 0:
        raise ValueError('Negative numbers can not be primes')
    # Base case
    if number <= 1:
        return 2

    # if even go back 1
    if number % 2 == 0:
        number -= 1
    while True:
        # only odds
        number += 2
        #only need to check up to and including the sqrt
        max_check = int(math.sqrt(number))+2
        # don't need to check even numbers
        for divider in range(3, max_check, 2):
            # if 'divider' divides 'number', then 'number' is not prime
            if number % divider == 0:
                break
        # if the for loop didn't break, then 'number' is prime
        else:
            return number

if __name__ == '__main__':
    number = int(sys.argv[1].strip())
    t0 = time.time()
    print('{0:d} is the next prime from {1:d}'.format(next_prime(number), number))
    run_time = time.time() - t0
    print('run_time = {0:.8f}'.format(run_time))
