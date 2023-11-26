import asyncio

async def example():
    p1 = await asyncio.create_subprocess_exec("sleep", "1")
    p2 = await asyncio.create_subprocess_exec("sleep", "2")
    p1_run = asyncio.create_task(p1.wait())
    p2_run = asyncio.create_task(p2.wait())
    pending = [p1_run, p2_run]
    while pending:
        done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)
        if p1_run in done:
            print("p1 finished, with status: ", p1.returncode)
        if p2_run in done:
            print("p2 finished, with status: ", p2.returncode)

asyncio.get_event_loop().run_until_complete(example())
