def auth_required(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        return func(*args, **kwargs) #DO NOT WAIT
    return wrapper

@app.post("/")
@auth_required # Custom decorator
def root(payload: SampleModel): #NOT ASYNC
    return {"message": "Hello World", "payload": payload}
