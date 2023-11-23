import inspect
import functools

# Global variable to store all functions decorated with @openaifunc
openai_functions = []

def openaifunc(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    # Get information about function parameters
    params = inspect.signature(func).parameters

    param_dict = dict()
    for k, v in params.items():
        # For simplicity, we assume all parameters are required
        # In real case, we need to inspect default values to find out optional parameters
        param_dict[k] = {
            "type": str(v.annotation),
            "description": "",  # This would need to be manually added or extracted from docstring
        }

    openai_functions.append({
        "name": func.__name__,
        "description": inspect.cleandoc(func.__doc__ or ""),
        "parameters": {
            "type": "object",
            "properties": param_dict,
            "required": list(param_dict.keys()),
        },
    })

    return wrapper

def get_openai_funcs():
    return openai_functions
