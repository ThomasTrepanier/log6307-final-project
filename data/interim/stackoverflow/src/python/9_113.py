from collections import defaultdict

def dd_rec():
    return defaultdict(dd_rec)

def defaultify(d):
    if not isinstance(d, dict):
        return d
    return defaultdict(dd_rec, {k: defaultify(v) for k, v in d.items()})

dd = defaultify(d)

key_lst = ["key1", "key2", "key5", "key6"]
value = "my_value2"
dd = set_nested_item(dd, key_lst, value)

print(dd)

# defaultdict(<function __main__.<lambda>>,
#             {'key1': defaultdict(<function __main__.<lambda>>,
#                          {'key2': defaultdict(<function __main__.<lambda>>,
#                                       {'key3': 'my_value',
#                                        'key5': defaultdict(<function __main__.<lambda>>,
#                                                    {'key6': 'my_value2'})})})})
