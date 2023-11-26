# app_cache.py
import os
from aiocache import Cache
from fastapi import FastAPI, status


app = FastAPI()
cache = Cache(Cache.REDIS, endpoint="localhost", port=6379, namespace="main")


class Meta:
    def __init__(self):
        pass

    async def get_count(self) -> int:
        return await cache.get("count", default=0)

    async def set_count(self, value: int) -> None:
        await cache.set("count", value)

    async def increment_count(self) -> None:
        await cache.increment("count", 1)


meta = Meta()


# increases the count variable in the meta object by 1
@app.post("/increment")
async def increment():
    await meta.increment_count()
    return status.HTTP_200_OK


# returns a json containing the current count from the meta object
@app.get("/report")
async def report():
    count = await meta.get_count()
    return {'count': count, "current_process_id": os.getpid()}


# resets the count in the meta object to 0
@app.post("/reset")
async def reset():
    await meta.set_count(0)
    return status.HTTP_200_OK
