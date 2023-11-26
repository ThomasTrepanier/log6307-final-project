import functools


class reprable:
    """Decorates a function with a repr method.

    Example:
        >>> @reprable
        ... def foo():
        ...     '''Does something cool.'''
        ...     return 4
        ...
        >>> foo()
        4
        >>> foo.__name__
        'foo'
        >>> foo.__doc__
        'Does something cool.'
        >>> repr(foo)
        'foo: Does something cool.'
        >>> type(foo)
        <class '__main__.reprable'>
    """

    def __init__(self, wrapped):
        self._wrapped = wrapped
        functools.update_wrapper(self, wrapped)

    def __call__(self, *args, **kwargs):
        return self._wrapped(*args, **kwargs)

    def __repr__(self):
        return f'{self._wrapped.__name__}: {self._wrapped.__doc__}'
