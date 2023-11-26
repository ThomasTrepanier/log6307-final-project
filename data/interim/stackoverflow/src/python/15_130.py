epislon = 5 

def extract_nested_values(it):
    if isinstance(it, list):
        for sub_it in it:
            yield from extract_nested_values(sub_it)
    elif isinstance(it, dict):
        for value in it.values():
            yield from extract_nested_values(value)
    else:
        yield it


d = {"foo": {"bar": 0.30000001}}
#[0.30000001]
e = {"foo": {"bar": 0.30000002}}
#[0.30000002]

d_value = list(extract_nested_values(d))
e_value = list(extract_nested_values(e))

if set(d.keys()) == set(e.keys()) and abs(e_value[0] - d_value[0]) < epislon:
    print('Close Enough')
else:
    print("not the same")
