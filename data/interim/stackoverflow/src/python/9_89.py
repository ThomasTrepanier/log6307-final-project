def average_dicts(dicts):
    result = {}
    for i, d in enumerate(dicts):
        for k, v in d.items():
            update_dict_average(result, k, v, i)
    return result

def update_dict_average(current, key, update, n):
    if isinstance(update, dict):
        subcurrent = current.setdefault(key, {})
        for subkey, subupdate in update.items():
            update_dict_average(subcurrent, subkey, subupdate, n)
    else:
        current[key] = (current.get(key, 0) * n + update) / (n + 1)

d = {'actor1': {'salary': {'year1': 60, 'year2': 65}, 'age': 30},
     'actor2': {'salary': {'year1': 20, 'year2': 30}, 'age': 17},
     'actor3': {'salary': {'year1': 50, 'year2': 80}, 'age': 25}}

result = {'average': average_dicts(d.values())}
print(result)
# {'average': {'salary': {'year1': 43.333333333333336, 'year2': 58.333333333333336}, 'age': 24.0}}
