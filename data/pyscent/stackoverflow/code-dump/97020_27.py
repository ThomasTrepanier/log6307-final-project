class MyRequestLoggingRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            body = await request.body()
            if body:
               logger.info(...)  # log request with body
            else:
               logger.info(...)  # log request without body
            try:

                return await original_route_handler(request)
            except RequestValidationError as exc:
               detail = {"errors": exc.errors(), "body": body.decode()}
               raise HTTPException(status_code=422, detail=detail)

        return custom_route_handler
