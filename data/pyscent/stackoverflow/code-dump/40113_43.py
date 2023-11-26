import re

def append_to(in_value, value_to_search, value_to_append):
    value_to_search = re.escape(value_to_search)
    return re.sub(
        '"({})"'.format(value_to_search),
        '"\\1{}"'.format(value_to_append),
        in_value,
    )

my_list = [append_to(item, 'value3', 'something_to_append') for item in my_list]
