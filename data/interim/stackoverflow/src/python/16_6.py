from functools import reduce


data_dictionary = {
    'foo': {
        'bar': {
            'buzz': 'lightyear'
        },
        'baz': {
            'asd': 2023,
            'zxc': [
                {'patrick': 'star'},
                {'spongebob': 'squarepants'}
            ],
            'qwe': ['john', 'sarah']
        }
    },
    'hello': {
        'world': 'hello world',
    },
}


def optional_chaining_v1(dictionary={}, *property_list):
    def reduce_callback(current_result, current_dictionary):
        if current_result is None:
            return dictionary.get(current_dictionary)
        if type(current_result) != dict:
            return None
        return current_result.get(current_dictionary)
    return reduce(reduce_callback, property_list, None)


# or in one line
optional_chaining_v1 = lambda dictionary={}, *property_list: reduce(lambda current_result, current_dictionary: dictionary.get(current_dictionary) if current_result is None else None if type(current_result) != dict else current_result.get(current_dictionary), property_list, None)

# usage
optional_chaining_v1_result1 = optional_chaining_v1(data_dictionary, 'foo', 'bar', 'baz')
print('optional_chaining_v1_result1:', optional_chaining_v1_result1)
optional_chaining_v1_result2 = optional_chaining_v1(data_dictionary, 'foo', 'bar', 'buzz')
print('optional_chaining_v1_result2:', optional_chaining_v1_result2)

# optional_chaining_v1_result1: None
# optional_chaining_v1_result2: lightyear


def optional_chaining_v2(dictionary={}, list_of_property_string_separated_by_dot=''):
    property_list = list_of_property_string_separated_by_dot.split('.')

    def reduce_callback(current_result, current_dictionary):
        if current_result is None:
            return dictionary.get(current_dictionary)
        if type(current_result) != dict:
            return None
        return current_result.get(current_dictionary)
    return reduce(reduce_callback, property_list, None)


# or in one line
optional_chaining_v2 = lambda dictionary={}, list_of_property_string_separated_by_dot='': reduce(lambda current_result, current_dictionary: dictionary.get(current_dictionary) if current_result is None else None if type(current_result) != dict else current_result.get(current_dictionary), list_of_property_string_separated_by_dot.split('.'), None)

# usage
optional_chaining_v2_result1 = optional_chaining_v2(data_dictionary, 'foo.bar.baz')
print('optional_chaining_v2_result1:', optional_chaining_v2_result1)
optional_chaining_v2_result2 = optional_chaining_v2(data_dictionary, 'foo.bar.buzz')
print('optional_chaining_v2_result2:', optional_chaining_v2_result2)

# optional_chaining_v2_result1: None
# optional_chaining_v2_result2: lightyear

