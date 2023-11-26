d = dict()
d['val'] = 5.78686876876089075543
d['name'] = 'kjbkjbkj'
d["mylist"] = [1.23456789, 12, 1.23, {"foo": "a", "bar": 9.87654321}]
d["mydict"] = {"bar": "b", "foo": 1.92837465}

# dump the object to a string
d_string = json.dumps(d, indent=4)

# find numbers with 8 or more digits after the decimal point
pat = re.compile(r"\d+\.\d{8,}")
def mround(match):
    return "{:.7f}".format(float(match.group()))

# write the modified string to a file
with open('test.json', 'w') as f:
    f.write(re.sub(pat, mround, d_string))
