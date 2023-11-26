from typing import Annotated
from fastapi import Depends
from pydantic import BaseModel, Field

class Model(BaseModel):
   query_param1: str = Field(...)
   query_param2: int | None = Field(None)


@app.get("")
async def _(query_params: Model = Depends()):
        ...
