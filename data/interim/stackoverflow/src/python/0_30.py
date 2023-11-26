@app.post("/items", response_model=Item)
async def post_item(item: Item = Depends()):
    ...

@app.patch("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: make_optional(Item) = Depends()):
    ...
