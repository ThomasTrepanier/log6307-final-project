def make_partial_model(model: Type[BaseModel], optional_fields: Optional[list[str]] = None) -> Type[BaseModel]:
    class NewModel(model):
        ...

    for field in NewModel.__fields__.values():
        if not optional_fields or field in optional_fields:
            field.required = False

    NewModel.__name__ = f'Partial{model.__name__}'
    return NewModel

PartialRequest = cast(Type[RequestModel], make_partial_model(RequestModel))
