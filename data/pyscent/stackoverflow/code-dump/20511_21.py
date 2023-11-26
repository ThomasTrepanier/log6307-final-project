#!/usr/bin/env python3
import os
import time
import random
from threading import Thread
from multiprocessing import Process, JoinableQueue


WORKERS = 4
DOWNLOADS_PER_SECOND = 2


def download_resource(url, resource_queue):
    pid = os.getpid()

    t = time.strftime('%H:%M:%S')
    print('Thread {p} is downloading from {u} ({t})'.format(p=pid, u=url, t=t),
          flush=True)
    time.sleep(random.randint(1, 10))

    results = '[resource {}]'.format(url)
    resource_queue.put(results)


def process_resource(resource_queue):
    pid = os.getpid()

    while True:
        res = resource_queue.get()

        print('Process {p} is processing {r}'.format(p=pid, r=res),
              flush=True)
        time.sleep(random.randint(1, 10))

        resource_queue.task_done()


def main():
    resource_queue = JoinableQueue()

    # Start process workers:
    for _ in range(WORKERS):
        worker = Process(target=process_resource,
                         args=(resource_queue,),
                         daemon=True)
        worker.start()

    urls = ['https://link/to/resource/{i}'.format(i=i) for i in range(10)]

    while urls:
        target_urls = urls[:DOWNLOADS_PER_SECOND]
        urls = urls[DOWNLOADS_PER_SECOND:]

        # Start downloader threads:
        for url in target_urls:
            downloader = Thread(target=download_resource,
                                args=(url, resource_queue),
                                daemon=True)
            downloader.start()

        time.sleep(1)

    resource_queue.join()


if __name__ == '__main__':
    main()
