array1 = ['key/value/one123904', 'key/value/two342389', 'key/value/three234093']
array2 = ['one', 'two', 'three', 'four']


def does_match_in_array_of_string(key: str, search_list : list) -> bool:
    for item in search_list:
        if key in item:
            return True
    return False;


match_failures = [key for key in array2 if not does_match_in_array_of_string(key, array1)]

if len(match_failures):
    print(f'No key for values: {match_failures}')
else:
    print('All keys have values')
