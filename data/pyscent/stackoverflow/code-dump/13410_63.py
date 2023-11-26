class IdentityComparableMethod:
    __slots__ = '_method',
    def __new__(cls, method):
        # Using __new__ prevents reinitialization, part of immutability contract
        # that justifies defining __hash__
        self = super().__new__(cls)
        self._method = method
        return self

    def __getattr__(self, name):
        '''Attribute access should match bound method's'''
        return getattr(self._method, name)

    def __eq__(self, other):
        '''Comparable to other instances, and normal methods'''
        if not isinstance(other, (IdentityComparableMethod, types.MethodType)):
            return NotImplemented
        return (self.__self__ is other.__self__ and
                self.__func__ is other.__func__)

    def __hash__(self):
        '''Hash identically to the method'''
        return hash(self._method)

    def __call__(self, *args, **kwargs):
        '''Delegate to method'''
        return self._method(*args, **kwargs)

    def __repr__(self):
        return '{0.__class__.__name__}({0._method!r})'.format(self)
