import asyncio
import threading

async def some_callback(args):
    await some_function()

def wrap_async_func(args):
    asyncio.run(some_callback(args))

_thread = threading.Thread(target=wrap_async_func, args=("some text"))
_thread.start()
