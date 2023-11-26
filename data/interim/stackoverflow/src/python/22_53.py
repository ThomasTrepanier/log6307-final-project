from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import itertools

def add_one(number, n):
    return number + 1 + n

def process():
    all_numbers = list(range(0, 10))

    with ThreadPoolExecutor(max_workers=10) as executor:
        
        for result in executor.map(add_one, all_numbers, itertools.repeat(2)):
            print(result)

process()
