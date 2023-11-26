import typing

def check_type(obj: typing.Any, type_to_check: typing.Any, _external=True) -> None:

    try:
        if not hasattr(type_to_check, "_name"):
            # base-case
            if not isinstance(obj, type_to_check):
                raise TypeError
            return
        # type_to_check is from typing library
        type_name = type_to_check._name

        if type_to_check is typing.Any:
            pass
        elif type_name in ("List", "Tuple"):
            if (type_name == "List" and not isinstance(obj, list)) or (
                type_name == "Tuple" and not isinstance(obj, tuple)
            ):
                raise TypeError

            element_type = type_to_check.__args__[0]
            for element in obj:
                check_type(element, element_type, _external=False)
        elif type_name == "Dict":
            if not isinstance(obj, dict):
                raise TypeError
            if len(type_to_check.__args__) != 2:
                raise NotImplementedError(
                    "check_type can only accept Dict typing with separate annotations for key and values"
                )
            key_type, value_type = type_to_check.__args__
            for key, value in obj.items():
                check_type(key, key_type, _external=False)
                check_type(value, value_type, _external=False)
        elif type_name is None and type_to_check.__origin__ is typing.Union:
            type_options = type_to_check.__args__
            no_option_matched = True
            for type_option in type_options:
                try:
                    check_type(obj, type_option, _external=False)
                    no_option_matched = False
                    break
                except TypeError:
                    pass
            if no_option_matched:
                raise TypeError
        else:
            raise NotImplementedError(
                f"check_type method currently does not support checking typing of form '{type_name}'"
            )

    except TypeError:
        if _external:
            raise TypeError(
                f"Object {repr(obj)} is of type {_construct_type_description(obj)} "
                f"when {type_to_check} was expected"
            )
        raise TypeError()


def _construct_type_description(obj) -> str:
    def get_types_in_iterable(iterable) -> str:
        types = {_construct_type_description(element) for element in iterable}
        return types.pop() if len(types) == 1 else f"Union[{','.join(types)}]"

    if isinstance(obj, list):
        return f"List[{get_types_in_iterable(obj)}]"
    elif isinstance(obj, dict):
        key_types = get_types_in_iterable(obj.keys())
        val_types = get_types_in_iterable(obj.values())
        return f"Dict[{key_types}, {val_types}]"
    else:
        return type(obj).__name__
