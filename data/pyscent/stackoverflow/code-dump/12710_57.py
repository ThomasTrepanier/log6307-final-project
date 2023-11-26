import asyncio
import time

async def process(semaphore, i):
    while True:
        print(f"{i} I'm gonna await")
        await asyncio.sleep(1)
        async with semaphore:
            print(f'{i} sleeping')
            await asyncio.sleep(3)
        print(f'{i} done sleeping')
        print(f"{i} I'm gonna await again")
        await asyncio.sleep(1)

async def other_process(semaphore):
    while True:
        while not semaphore.locked():
            print("Everyone is awaiting... but I'm not startingr")
            await asyncio.sleep(1)
        print("Everyone is busy, let's do this!")
        time.sleep(5)
        print('5 seconds are up, let everyone else play again')
        await asyncio.sleep(1)

semaphore = asyncio.Semaphore(10)
dataset = [i for i in range(10)]
loop = asyncio.new_event_loop()
tasks = [loop.create_task(process(semaphore, i)) for i in dataset]
tasks.append(loop.create_task(other_process(semaphore)))
loop.run_until_complete(asyncio.wait(tasks))

