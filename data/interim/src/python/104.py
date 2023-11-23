import asyncio
import ijson

async def remove_keys(obj):
    """Asynchronously remove keys starting with '_' from an object"""
    if isinstance(obj, dict):
        return {k: await remove_keys(v) for k, v in obj.items() if not k.startswith('_')}
    elif isinstance(obj, list):
        return [await remove_keys(item) for item in obj]
    else:
        return obj

async def transform_json(json_stream):
    parser = ijson.parse_async(json_stream)
    items = ijson.items_async(parser, 'item')

    async for item in items:
        yield await remove_keys(item)

async def test():
    async def json_stream():
        chunks = [
            b'{"item": {"_id": 1, "name": "test1"}},',
            b'{"item": {"_id": 2, "name": "test2"}},',
            b'{"item": {"_id": 3, "name": "test3"}}'
        ]
        for chunk in chunks:
            yield chunk
            await asyncio.sleep(0.1)

    async for transformed_item in transform_json(json_stream()):
        print(transformed_item)

# Run the test coroutine
asyncio.run(test())
