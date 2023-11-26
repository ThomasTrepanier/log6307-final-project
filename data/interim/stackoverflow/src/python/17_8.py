# imports
from typing import Union
from pydantic import BaseModel
from fastapi import Depends, Request

# the base model
class QueryParams(BaseModel):
    required: str
    optional: Union[None, str] = None
    dynamic: dict

# dependency
async def query_params(
    request: Request, requiredParam1: str, optionalParam1: Union[None, str] = None
    ):
    # process the request here
    dynamicParams = {}
    for k in request.query_params.keys():
        if 'dynamicParam' not in k:
            continue
        dynamicParams[k] = request.query_params[k]

    # also maybe do some other things on the arguments
    # ...

    return {
        'required': requiredParam1,
        'optional': optionalParam1,
        'dynamic': dynamicParams
    }

# the endpoint
@app.get("api/")
async def hello(params: QueryParams = Depends(query_params)):

    # Maybe do domething with params here,
    # Use it as you would any BaseModel object
    # ...

    return params

