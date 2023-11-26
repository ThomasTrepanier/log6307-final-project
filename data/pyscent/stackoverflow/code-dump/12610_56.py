async def do_stuff(semaphore):
    async with semaphore:
      await getting_stuff_done()

async def wait_til_everyone_is_busy(semaphore):
    while not semaphore.locked():
      await asyncio.sleep(1)
    do_other_stuff()
