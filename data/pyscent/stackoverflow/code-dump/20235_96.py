import json

def find_values(id, json_file):
    results = []

    def _decode_dict(a_dict):
        try:
            results.append(a_dict[id])
        except KeyError:
            pass
        return a_dict

    json.load(json_file, object_hook=_decode_dict)  # Return value ignored.
    return len(results) > 0  # If there are any results, id was found.

with open('find_key_test.json', 'r') as json_file:
    print(find_values('post', json_file)) # -> True
