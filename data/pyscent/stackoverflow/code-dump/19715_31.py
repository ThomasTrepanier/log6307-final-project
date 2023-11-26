array_of_dicts = [{"a": 1, "b": 2}, {"a": 1, "b": "zz"}, {"a": 1, "b": "2"}]

def is_entry_in_all_dicts(key, value):
    identical_entries_found = 0
    for dict in array_of_dicts:
        if key in dict:
            if dict[key] == value:
                identical_entries_found += 1
    if identical_entries_found == len(array_of_dicts):
        return True
    return False
                
result = []
for dict in array_of_dicts:
    for key, value in dict.items():
        if is_entry_in_all_dicts(key, value):
            if key not in result:
                result.append(key)
print(result)
