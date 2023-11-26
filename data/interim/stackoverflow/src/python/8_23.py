import time
import pymongo
import json
import asyncio
from aiohttp import ClientSession


async def get_url(url, session):
    async with session.get(url) as response:
        if response.status == 200:
            return await response.text()


async def create_task(sem, url, session):
    async with sem:
        response = await get_url(url, session)
        if response:
            parsed = json.loads(response)
            n = url.rsplit('/', 1)[1]
            inserted = com.insert_one(parsed)
            write_log.write(str(n) + "\t" + str(inserted) + "\n")
            print(str(n) + "\t" + str(inserted) + "\n")


async def run(minimum, maximum):
    url = 'https:/xx.xxx.xxx/{}.json'
    tasks = []
    sem = asyncio.Semaphore(1000)   # Maximize the concurrent sessions to 1000, stay below the max open sockets allowed
    async with ClientSession() as session:
        for n in range(minimum, maximum):
            task = asyncio.ensure_future(create_task(sem, url.format(n), session))
            tasks.append(task)
        responses = asyncio.gather(*tasks)
        await responses


client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
db = client["thread1"]
com = db["threadcol"]
start_time = time.time()
write_log = open("logging.log", "a")
min_item = 1
max_item = 100

loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run(min_item, max_item))
loop.run_until_complete(future)
write_log.close()
