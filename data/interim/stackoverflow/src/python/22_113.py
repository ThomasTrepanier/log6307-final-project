def do_stuff():
    # create a generator based coroutine
    # cannot mix syntax of asyncio
    ioBoundTask = do_iobound_work_async()
    ioBoundResult = yield from ioBoundTask
    # whatever
