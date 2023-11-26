#!/usr/bin/env python3
import os
import time
import random
from functools import partial
from multiprocessing import Pool, Manager


CPU_NUM = 4
CONCURRENT_DOWNLOADS = 2


def download(url, semaphore):
    pid = os.getpid()

    with semaphore:
        print('Process {p} is downloading from {u}'.format(p=pid, u=url))
        time.sleep(random.randint(1, 5))

    # Process the obtained resource:
    time.sleep(random.randint(1, 5))

    return 'Successfully processed {}'.format(url)


def main():
    manager = Manager()

    semaphore = manager.Semaphore(CONCURRENT_DOWNLOADS)
    target = partial(download, semaphore=semaphore)

    urls = ['https://link/to/resource/{i}'.format(i=i) for i in range(10)]

    with Pool(processes=CPU_NUM) as pool:
        results = pool.map(target, urls)

    print(results)


if __name__ == '__main__':
    main()
