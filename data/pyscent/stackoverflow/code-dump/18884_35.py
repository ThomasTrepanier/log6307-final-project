import asyncio


async def delay(n):
    print(f"sleeping for {n} second(s)")
    await asyncio.sleep(n)
    print(f"done sleeping for {n} second(s)")


async def main():
    t1 = asyncio.create_task(delay(1))
    t2 = asyncio.create_task(delay(2))
    await t2


asyncio.run(main())
