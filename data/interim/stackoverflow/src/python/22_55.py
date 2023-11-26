from concurrent.futures import ThreadPoolExecutor, as_completed

def add_one(args):
    return args[0] + 1 + args[1]

def process():
    all_numbers = []
    for i in range(0, 10):
        all_numbers.append([i, 2])

    all_results = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        for i in executor.map(add_one, all_numbers):
            print(i)
            all_results.append(i)

    for index, result in enumerate(all_results):
        print(result)

process()
