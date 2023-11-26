from concurrent.futures import ThreadPoolExecutor, as_completed

def add_one(number, n):
    return number + 1 + n

def process():
    all_numbers = []
    for i in range(0, 10):
        all_numbers.append(i)

    threads = []
    all_results = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        for number in all_numbers:
            threads.append(executor.submit(add_one, number))

        for index, task in enumerate(threads):
            result = task.result()
            #print(result)
            all_results.append(result)

    for index, result in enumerate(all_results):
        print(result)

process()
