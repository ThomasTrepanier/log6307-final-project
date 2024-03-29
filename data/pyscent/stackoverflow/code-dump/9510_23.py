def getKeys(object, prev_key = None, keys = []):
    if type(object) != type({}):
        keys.append(prev_key)
        return keys
    new_keys = []
    for k, v in object.items():
        if prev_key != None:
            new_key = "{}.{}".format(prev_key, k)
        else:
            new_key = k
        new_keys.extend(getKeys(v, new_key, []))
    return new_keys
