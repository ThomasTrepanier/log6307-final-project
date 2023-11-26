import asyncio
from tqdm.asyncio import tqdm
import random

async def factorial(name, number):
    f = 1
    for i in range(2, number+1):
        await asyncio.sleep(random.random())
        f *= i
    print(f"Task {name}: factorial {number} = {f}")


async def main():
    # Schedule the three concurrently

    flist = [factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4)]

    await tqdm.gather(*flist)

asyncio.run(main())
