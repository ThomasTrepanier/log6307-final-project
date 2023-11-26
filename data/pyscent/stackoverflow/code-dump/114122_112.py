async def do_stuff():
    ioBoundTask = do_iobound_work_async() # created a coroutine
    ioBoundResult = await ioBoundTask     # start the coroutine
    cpuBoundResult = do_cpu_intensive_calc()
    print(f"The result is {cpuBoundResult + ioBoundResult}")
