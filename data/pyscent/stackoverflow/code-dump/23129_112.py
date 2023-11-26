from functools import reduce
from operator import getitem

def set_nested_item(dataDict, mapList, val):
    """Set item in nested dictionary"""
    reduce(getitem, mapList[:-1], dataDict)[mapList[-1]] = val
    return dataDict

key_lst = ["key1", "key2", "key3"]
value = "my_value"
d = {"key1": {"key2": {"key3": "some_value"}}}

d = set_nested_item(d, key_lst, value)

print(d)
# {'key1': {'key2': {'key3': 'my_value'}}}
