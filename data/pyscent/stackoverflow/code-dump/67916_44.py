class ParentBase(BaseModel):
    """Shared properties."""
    name: str
    email: str

class ParentCreate(ParentBase):
    """Properties to receive on item creation."""
    # dont need id here if your db autocreates it
    pass

class ParentUpdate(ParentBase):
    """Properties to receive on item update."""
    # dont need id as you are likely PUTing to /parents/{id}
    # other fields should not be optional in a PUT
    # maybe what you are wanting is a PATCH schema?
    pass

class ParentInDBBase(ParentBase):
    """Properties shared by models stored in DB - !exposed in create/update."""
    # primary key exists in db, but not in base/create/update
    id: int                             

class Parent(ParentInDBBase):
    """Properties to return to client."""
    # optionally include things like relationships returned to consumer
    # related_things: List[Thing]
    pass

class ParentInDB(ParentInDBBase):
    """Additional properties stored in DB."""
    # could be secure things like passwords?
    pass
