import asyncio


async def delay(n):
    print(f"sleeping for {n} second(s)")
    await asyncio.sleep(n)
    print(f"done sleeping for {n} second(s)")


loop = asyncio.get_event_loop()
t1 = loop.create_task(delay(1))
t2 = loop.create_task(delay(2))
loop.run_until_complete(t1)

pending = asyncio.all_tasks(loop=loop)
group = asyncio.gather(*pending)
loop.run_until_complete(group)

loop.close()
