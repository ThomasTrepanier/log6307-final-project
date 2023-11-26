from functools import wraps
from inspect import signature
from typing import Callable, ParamSpec, TypeVar, TYPE_CHECKING

T = TypeVar("T")
P = ParamSpec("P")


def check_args(func: Callable[P, T]) -> Callable[P, T]:
    """
    Decorator to monitor whether an argument is passed
    positionally or with its keyword, during function call.
    """

    @wraps(func)
    def inner(*args: P.args, **kwargs: P.kwargs) -> T:
        for param in signature(func).parameters:
            if param in kwargs:
                print(param, 'passed with its keyword!')
            else:
                print(param, 'passed positionally.')
        return func(*args, **kwargs)

    return inner
