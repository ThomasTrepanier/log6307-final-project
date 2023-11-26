from fastapi import FastAPI, Depends
from pydantic import create_model

app = FastAPI()

# Put your query arguments in this dict
query_params = {"name": (str, "me")}

query_model = create_model("Query", **query_params) # This is subclass of pydantic BaseModel

# Create a route
@app.get("/items")
async def get_items(params: query_model = Depends()):
    params_as_dict = params.dict()
    ...
