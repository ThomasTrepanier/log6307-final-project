import asyncio

async def coroutine():
    print('in coroutine')

coro = coroutine()
event_loop = asyncio.get_event_loop()

event_loop.run_until_complete(coro)
event_loop.close()
