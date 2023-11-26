def wrap_type(obj, kind, wrapper):
    """ Recursively wrap instances of type kind in dictionary and list
        objects.
    """
    if isinstance(obj, dict):
        new_dict = {}
        for key, value in obj.items():
            if not isinstance(value, (dict, list)):
                new_dict[key] = wrapper(value) if isinstance(value, kind) else value
            else:
                new_dict[key] = wrap_type(value, kind, wrapper)
        return new_dict

    elif isinstance(obj, list):
        new_list = []
        for value in obj:
            if not isinstance(value, (dict, list)):
                new_list.append(wrapper(value) if isinstance(value, kind) else value)
            else:
                new_list.append(wrap_type(value, kind, wrapper))
        return new_list

    else:
        return obj


d = dict()
d['val'] = 5.78686876876089075543
d['name'] = 'kjbkjbkj'

with open('float_test.json', 'w') as file:
    json.dump(wrap_type(d, float, FloatWrapper), file, cls=MyEncoder, indent=4)
