def display_function(func):
    """ This decorator prints before and after running """

    @functools.wraps(func)
    def function_wrapper(*args, **kwargs):
        print(f'\nNow: Calling {func.__name__}.')
        entity = func(*args, **kwargs)
        print(f'Done: Calling {func.__name__}.\n')
        return entity

    return function_wrapper
