# app_db.py
from fastapi import FastAPI, status
from tortoise import Model, fields
from tortoise.contrib.fastapi import register_tortoise


class MetaModel(Model):
    count = fields.IntField(default=0)


app = FastAPI()


# increases the count variable in the meta object by 1
@app.post("/increment")
async def increment():
    meta, is_created = await MetaModel.get_or_create(id=1)
    meta.count += 1  # it's better do it in transaction
    await meta.save()
    return status.HTTP_200_OK


# returns a json containing the current count from the meta object
@app.get("/report")
async def report():
    meta, is_created = await MetaModel.get_or_create(id=1)
    return {'count': meta.count}


# resets the count in the meta object to 0
@app.post("/reset")
async def reset():
    meta, is_created = await MetaModel.get_or_create(id=1)
    meta.count = 0
    await meta.save()
    return status.HTTP_200_OK

register_tortoise(
    app,
    db_url="postgres://test_user:test_pass@localhost:5432/test_db",  # Don't expose login/pass in src, use environment variables
    modules={"models": ["app_db"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
