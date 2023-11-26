import asyncio


async def startit(thing):
    t = asyncio.create_task(thing)
    # what we really need to do here is:
    # Insert t into runnable queue, just before asyncio.current_task(), and switch to it.
    # Only, it is not possible since event loops are just about scheduling callbacks
    await asyncio.sleep(0)
    return t


async def fa():
    print('fa start')
    gb = await startit(fb())
    # send off a hTTP request and wait for it
    print ('fa doing blocking thing')
    await asyncio.sleep(0.1)
    print ('fa waiting for gb')
    await gb
    print ('fa stopping')
    return 'a'

async def fb():
    print('fb start')
    # send off another http request and wait for it
    await asyncio.sleep(0.1)
    print('fb stop')
    return 'b'


async def main():
    
    print('main start')
    ga = await startit(fa())
    print("main waiting for a")
    await ga
    print('main done')

asyncio.run(main())
