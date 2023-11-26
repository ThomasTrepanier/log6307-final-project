from concurrent.futures import ThreadPoolExecutor, as_completed


def add_one(number, index):
    return number + 1, index


def process():
    all_numbers = []
    for i in range(0, 10):
        all_numbers.append(i)

    threads = []
    all_results = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        for index, number in enumerate(all_numbers):
            threads.append(executor.submit(add_one, number, index))
        for task in as_completed(threads):
            result, index = task.result()
            all_results.append([result, index])
        all_results = sorted(all_results, key=lambda x: x[-1])

    for index, result in enumerate(all_results):
        print(result[0])


process()
