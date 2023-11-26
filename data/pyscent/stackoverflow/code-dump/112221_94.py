def replace_exception_chars(string):
    exception_chars_dict = {'Old': 'New', 'old': 'new'}
    exception_chars_keys = list(exception_chars_dict.keys())
    for exception_char in exception_chars_keys:
        if exception_char in string:
            string = string.replace(
                exception_char, exception_chars_dict[exception_char])
    return string


print(replace_exception_chars('Old, not old'))
# New, not new
