def get_val(data, keys):
    try:
        for k in keys:
            data = data[k]
        return data
    except (KeyError, AttributeError) as e:
        return ""

dictionary2 = {"required": {"value1": "one", "value2": "two"}}
print(get_val(dictionary2, ("required", "value2")))
print(get_val(dictionary2, ("optional", "value1")))
