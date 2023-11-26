def remove_defaults(baseclass: Type[T]) -> Type[T]:
    validators = {"__validators__": baseclass.__validators__}
    fields = baseclass.__fields__

    def remove_default(item: pydantic.fields.ModelField) -> pydantic.fields.FieldInfo:
        info = item.field_info
        if info.default == pydantic.fields.Undefined and not info.default_factory:
            raise RuntimeError("Field has no default")

        # Funny enough, if we don't keep the default for Optional types,
        # openapi-generator will not make it optional at all.
        if item.allow_none:
            return copy.copy(item.field_info)

        return pydantic.Field(
            alias=item.field_info.alias,
            title=item.field_info.title,
            description=item.field_info.description,
            exclude=item.field_info.exclude,
            include=item.field_info.include,
            const=item.field_info.const,
            gt=item.field_info.gt,
            ge=item.field_info.ge,
            lt=item.field_info.lt,
            le=item.field_info.le,
            multiple_of=item.field_info.multiple_of,
            allow_inf_nan=item.field_info.allow_inf_nan,
            max_digits=item.field_info.max_digits,
            decimal_places=item.field_info.decimal_places,
            min_items=item.field_info.min_items,
            max_items=item.field_info.max_items,
            unique_items=item.field_info.unique_items,
            min_length=item.field_info.min_length,
            max_length=item.field_info.max_length,
            allow_mutation=item.field_info.allow_mutation,
            regex=item.field_info.regex,
            discriminator=item.field_info.discriminator,
            repr=item.field_info.repr,
        )

    nondefault_fields = {
        key: (item.type_, remove_default(item)) for key, item in fields.items()
    }

    return pydantic.create_model(
        __model_name=f"{baseclass.__name__}Optional",
        __base__=baseclass,
        __validators__=validators,
        **nondefault_fields,
    )


class PatchPoll(pydantic.BaseModel):
    id: UUID = pydantic.Field(default_factory=uuid4)
    subject: str = pydantic.Field(max_length=1024, default="")
    description: Optional[str] = pydantic.Field(max_length=1024 * 1024, default="")


class Poll(remove_defaults(PatchPoll)):
    ...
