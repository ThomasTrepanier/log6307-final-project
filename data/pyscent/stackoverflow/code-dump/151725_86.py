def json_loader(schema, json):
    try:
        assert json is not None, "request body is required"
    except AssertionError as assertionError:
        raise InvalidUsage(40001, assertionError.args[0], 400)
    result = schema.load(json)
    if result.errors:
        raise InvalidUsage(40001, result.errors, 400)
    else:
        return result.data
