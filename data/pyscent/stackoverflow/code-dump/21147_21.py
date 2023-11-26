def copy_dict(original, keys=None):
    keys = keys or {key for key in original}
    return {
        key: value for key, value in original if key in keys
    }

mydict = {
    "color":"green",
    "type":"veg",
    "fruit":"apple",
    "level": 5
}
new_dict = copy_dict(mydict, {'color', 'fruit'})
