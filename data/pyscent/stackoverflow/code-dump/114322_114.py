async def do_cpu_intensive_calc():
    print("Do smart calc...")
    await asyncio.sleep(2)
    print("Calc finished.")
    return 2

# 2.5s
async def do_stuff():
    task1 = asyncio.create_task(do_iobound_work_async())
    task2 = asyncio.create_task(do_cpu_intensive_calc())

    ioBoundResult = await task1
    cpuBoundResult = await task2
    print(f"The result is {cpuBoundResult + ioBoundResult}")
