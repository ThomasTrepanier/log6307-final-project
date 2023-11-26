async def wait_and_return_original(proc: asyncio.subprocess):
    await proc.wait()
    return proc

async def example2():
    p1 = await asyncio.create_subprocess_exec("sleep", "1")
    p2 = await asyncio.create_subprocess_exec("sleep", "2")
    
    for p in asyncio.as_completed([wait_and_return_original(p) for p in [p1, p2]]):
        p_completed = await p   # NOTE: for-loop iteration variable doesn't decide which task is first completed until here!
        if p_completed is p1:
            print("p1 finished, with status: ", p1.returncode)
        if p_completed is p2:
            print("p2 finished, with status: ", p2.returncode)

asyncio.get_event_loop().run_until_complete(example2())
