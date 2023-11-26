from fastapi import APIRouter, FastAPI, Request, Response, Body
from fastapi.routing import APIRoute

from typing import Callable, List
from uuid import uuid4


class ContextIncludedRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            request_id = str(uuid4())
            response: Response = await original_route_handler(request)

            if await request.body():
                print(await request.body())

            response.headers["Request-ID"] = request_id
            return response

        return custom_route_handler


app = FastAPI()
router = APIRouter(route_class=ContextIncludedRoute)


@router.post("/context")
async def non_default_router(bod: List[str] = Body(...)):
    return bod


app.include_router(router)
