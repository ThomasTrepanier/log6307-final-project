@openaifunc
def add_numbers(a: int, b: int):
    """
    This function adds two numbers.
    """
    return a + b

@openaifunc
def say_hello(name: str):
    """
    This function greets the user.
    """
    return f"Hello, {name}!"

print(get_openai_funcs())
