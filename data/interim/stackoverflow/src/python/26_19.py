import platform
from functools import wraps
from typing import Callable, Optional


def implement_for_os(os_name: str):
    """
    Produce a decorator that defines a function only if the
    platform returned by `platform.system` matches the given `os_name`.
    Otherwise, replace the function with one that raises `NotImplementedError`.
    """
    def decorator(previous_definition: Optional[Callable]):
        def _decorator(func: Callable):
            if previous_definition and hasattr(previous_definition, '_implemented_for_os'):
                # This function was already implemented for this platform. Leave it unchanged.
                return previous_definition
            elif platform.system() == os_name:
                # The current function is the correct impementation for this platform.
                # Mark it as such, and return it unchanged.
                func._implemented_for_os = True
                return func
            else:
                # This function has not yet been implemented for the current platform
                @wraps(func)
                def _not_implemented(*args, **kwargs):
                    raise NotImplementedError(
                        f"The function {func.__name__} is not defined"
                        f" for the platform {platform.system()}"
                    )

                return _not_implemented
        return _decorator

    return decorator


implement_linux = implement_for_os('Linux')

implement_windows = implement_for_os('Windows')
