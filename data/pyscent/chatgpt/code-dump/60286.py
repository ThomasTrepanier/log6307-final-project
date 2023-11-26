import asyncio
import ijson
from concurrent.futures import ThreadPoolExecutor

def parse_json(json_stream):
    items = ijson.items(json_stream, item_path='item')
    for item in items:
        yield {k: v for k, v in item.items() if not k.startswith('_')}

async def transform_json(async_generator):
    with ThreadPoolExecutor(max_workers=1) as executor:
        loop = asyncio.get_event_loop()

        async for chunk in async_generator:
            yield await loop.run_in_executor(executor, parse_json, chunk)

async def test():
    async def json_generator():
        chunks = [
            '{"item": {"_id": 1, "name": "test1"}},',
            '{"item": {"_id": 2, "name": "test2"}},',
            '{"item": {"_id": 3, "name": "test3"}}'
        ]
        for chunk in chunks:
            yield chunk
            await asyncio.sleep(0.1)

    async for transformed_chunk in transform_json(json_generator()):
        print(transformed_chunk)

# Run the test coroutine
asyncio.run(test())
