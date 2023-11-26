async def test(name):
    await asyncio.sleep(5)
    return f"hello {name}"

run_async(test, "user")  # blocks for 5 seconds and returns "hello user"
