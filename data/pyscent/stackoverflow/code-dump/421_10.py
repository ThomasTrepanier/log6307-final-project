class Model(BaseModel):
    the_id: UUID = Field(default_factory=uuid4)

print(Model().model_dump(mode='json'))
# {'the_id': '4c94e7bc-78fe-48ea-8c3b-83c180437774'}
