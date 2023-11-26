from fastapi import FastAPI, Request
from starlette.responses import RedirectResponse

app = FastAPI()

@app.get("/data/")
async def api_data(request: Request):
    params = request.query_params
    url = f'http://some.other.api/?{params}'
    response = RedirectResponse(url=url)
    return response
