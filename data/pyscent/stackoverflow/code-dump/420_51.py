@app.patch('/items/{item_id}', response_model=Item)
async def update_item(item_id: str, item: Item):
    update_item_values = item.dict(exclude_defaults=True, exclude_none=True)

    # Get intersection of keys/fields
    # Must have at least 1 common
    if not (set(update_item_values.keys()) & set(Item.__fields__)):
        raise HTTPException(status_code=400, detail='No common fields')

    update_item = Item(**update_item_values)

    return update_item
