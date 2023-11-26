def default_kwargs(**default):
    from functools import wraps
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            from inspect import getfullargspec
            f_args = getfullargspec(f)[0]
            used_args = f_args[:len(args)]

            final_kwargs = {
                key: value 
                for key, value in {**default, **kwargs}.items() 
                if key not in used_args
            }

            return f(*args, **final_kwargs)
        return wrapper
    return decorator
