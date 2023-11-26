class CopyRequestMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_body = await request.json()
        request.state.body = request_body

        response = await call_next(request)
        return response

class LogRequestMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Since it'll be loaded after CopyRequestMiddleware it can access request.state.body.
        request_body = request.state.body
        print(request_body)
    
        response = await call_next(request)
        return response
